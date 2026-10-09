import pandas as pd
import yfinance as yf

from stockmind.application.history.daily_buy_signal_evaluator import DailyBuySignalEvaluator
from stockmind.application.history.refresh_buy_periods_use_case import RefreshBuyPeriodsUseCase
from stockmind.application.use_cases.run_analysis_use_case import RunAnalysisUseCase
from stockmind.domain.history.historical_setup_entry import HistoricalSetupEntry
from stockmind.domain.history.historical_outcome import evaluate_price_window
from stockmind.domain.indicators.indicator_result import IndicatorResult
from stockmind.infrastructure.history.daily_buy_signal_repository import DailyBuySignalRepository
from stockmind.infrastructure.history.historical_setup_repository import HistoricalSetupRepository
from stockmind.infrastructure.history.historical_opportunity_repository import HistoricalOpportunityRepository
from stockmind.infrastructure.history.buy_period_repository import BuyPeriodRepository
from stockmind.infrastructure.profiles.profile_repository import ProfileRepository

PROFILES=["conservative","balanced","aggressive"]


class TrueIncrementalSymbolRefreshUseCase:
    def execute(self, symbol: str):
        symbol=symbol.upper().strip()
        raw=yf.Ticker(symbol).history(period="5y").copy()
        if raw.empty:
            return
        if raw.index.tz is not None:
            raw.index=raw.index.tz_localize(None)
        raw=raw.sort_index()
        prepared=self._prepare(raw)
        latest_date=prepared.index[-1].date().isoformat()

        for profile_name in PROFILES:
            self._append_daily_signal(symbol,profile_name,prepared,latest_date)
            self._refresh_incomplete_setups(symbol,profile_name,prepared)
            # Period builder is deterministic and reads persisted BUY signals/setups. This rebuilds only one canonical 5y set,
            # without recomputing all indicator days.
            RefreshBuyPeriodsUseCase().execute(symbol,profile_name,"5y",3,.08)
            self._refresh_incomplete_opportunities(symbol,profile_name,raw)
            # Current analysis persists latest dashboard state. It remains the remaining heavy current-analysis call.
            RunAnalysisUseCase().execute(profile_name=profile_name,symbol=symbol)

    def _append_daily_signal(self,symbol,profile_name,data,latest_date):
        repo=DailyBuySignalRepository()
        if repo.get_latest_date(symbol,profile_name,"5y")==latest_date:
            return
        row=data.iloc[-1]
        if not self._valid(row):
            return
        indicator=IndicatorResult(symbol=symbol,values={
            "rsi_14":float(row["rsi_14"]),"sma_20":float(row["sma_20"]),"ema_20":float(row["ema_20"]),
            "macd":float(row["macd"]),"bollinger_position":float(row["bollinger_position"]),
            "adx_14":float(row["adx_14"]),"stoch_k_14":float(row["stoch_k_14"]),
        })
        signal=DailyBuySignalEvaluator().evaluate(
            symbol=symbol,profile=ProfileRepository().get_by_name(profile_name),analysis_period="5y",
            trading_date=latest_date,entry_price=float(row["Close"]),indicator_result=indicator,
        )
        repo.upsert(signal)
        if signal.is_buy:
            evaluation=evaluate_price_window(data[["High","Low","Close"]],latest_date,signal.entry_price,.08,60,1.0)
            HistoricalSetupRepository().upsert(HistoricalSetupEntry(
                symbol,profile_name,"5y",latest_date,signal.entry_price,.08,evaluation.target_hit,
                evaluation.days_to_target,evaluation.max_gain_pct,evaluation.max_drawdown_pct,
                evaluation.window_start_date,evaluation.window_end_date,evaluation.window_end_return_pct,
                evaluation.outcome.value,evaluation.is_complete,
            ))

    def _refresh_incomplete_setups(self,symbol,profile_name,data):
        repo=HistoricalSetupRepository()
        for entry in repo.load_incomplete(symbol,profile_name,"5y"):
            evaluation=evaluate_price_window(data[["High","Low","Close"]],entry.setup_date,entry.entry_price,entry.target_pct,60,1.0)
            repo.upsert(HistoricalSetupEntry(
                entry.symbol,entry.profile_name,entry.analysis_period,entry.setup_date,entry.entry_price,entry.target_pct,
                evaluation.target_hit,evaluation.days_to_target,evaluation.max_gain_pct,evaluation.max_drawdown_pct,
                evaluation.window_start_date,evaluation.window_end_date,evaluation.window_end_return_pct,
                evaluation.outcome.value,evaluation.is_complete,
            ))

    def _refresh_incomplete_opportunities(self,symbol,profile_name,raw):
        # Preserve the historical score itself; update only the later validation outcome.
        repo=HistoricalOpportunityRepository()
        updated=[]
        for entry in repo.load_incomplete(symbol,profile_name):
            price_row=raw.loc[raw.index.normalize()==pd.Timestamp(entry.trading_date)]
            if price_row.empty:
                continue
            evaluation=evaluate_price_window(raw[["High","Low","Close"]],entry.trading_date,float(price_row["Close"].iloc[-1]),.08,60,1.0)
            updated.append(type(entry)(
                entry.symbol,entry.profile_name,entry.trading_date,entry.opportunity_score,entry.confidence,
                entry.historical_success_rate,entry.historical_sample_count,entry.historical_source,entry.risk_level,
                entry.signal,entry.quality,entry.quality_component,entry.confidence_component,entry.historical_component,
                entry.risk_component,evaluation.outcome.value,evaluation.is_complete,evaluation.days_to_target,
                evaluation.max_gain_pct,evaluation.max_drawdown_pct,
            ))
        repo.upsert_entries(updated)

    def _prepare(self,data):
        p=data.copy();p["sma_20"]=p["Close"].rolling(20).mean();p["ema_20"]=p["Close"].ewm(span=20).mean()
        delta=p["Close"].diff();gain=delta.where(delta>0,0).rolling(14).mean();loss=-delta.where(delta<0,0).rolling(14).mean();p["rsi_14"]=100-(100/(1+gain/loss))
        p["macd"]=p["Close"].ewm(span=12).mean()-p["Close"].ewm(span=26).mean();mean=p["Close"].rolling(20).mean();std=p["Close"].rolling(20).std();p["bollinger_position"]=(p["Close"]-(mean-2*std))/(4*std)
        high,low,close=p["High"],p["Low"],p["Close"];up=high.diff();down=low.shift(1)-low;plus=up.where((up>down)&(up>0),0.0);minus=down.where((down>up)&(down>0),0.0);prev=close.shift(1);tr=pd.concat([high-low,(high-prev).abs(),(low-prev).abs()],axis=1).max(axis=1);atr=tr.rolling(14).mean();pdi=100*plus.rolling(14).mean()/atr;mdi=100*minus.rolling(14).mean()/atr;p["adx_14"]=(100*(pdi-mdi).abs()/(pdi+mdi)).rolling(14).mean();lo=low.rolling(14).min();hi=high.rolling(14).max();p["stoch_k_14"]=100*(close-lo)/(hi-lo);return p
    def _valid(self,row):
        return all(not pd.isna(row[c]) for c in ["Close","High","Low","rsi_14","sma_20","ema_20","macd","bollinger_position","adx_14","stoch_k_14"])
