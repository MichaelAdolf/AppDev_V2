from dataclasses import dataclass
import pandas as pd
import yfinance as yf
from stockmind.application.history.daily_buy_signal_evaluator import DailyBuySignalEvaluator
from stockmind.application.history.historical_opportunity_replay_use_case import HistoricalOpportunityReplayUseCase
from stockmind.application.history.refresh_buy_periods_use_case import RefreshBuyPeriodsUseCase
from stockmind.domain.history.historical_outcome import evaluate_price_window
from stockmind.domain.history.historical_setup_entry import HistoricalSetupEntry
from stockmind.domain.indicators.indicator_result import IndicatorResult
from stockmind.infrastructure.history.daily_buy_signal_repository import DailyBuySignalRepository
from stockmind.infrastructure.history.historical_setup_repository import HistoricalSetupRepository
from stockmind.infrastructure.profiles.profile_repository import ProfileRepository

@dataclass(frozen=True)
class IndividualHistoryBackfillResult:
    symbol:str;signal_count:int;buy_signal_count:int;setup_count:int;period_count:int;opportunity_count:int

class IndividualHistoryBackfillUseCase:
    ANALYSIS_PERIOD='5y'
    def execute(self,symbol):
        symbol=symbol.upper().strip();raw=yf.Ticker(symbol).history(period=self.ANALYSIS_PERIOD).copy()
        if raw.empty:raise ValueError(f'Keine historischen Marktdaten für {symbol} vorhanden.')
        if raw.index.tz is not None:raw.index=raw.index.tz_localize(None)
        raw=raw.sort_index();prepared=self._prepare(raw);profile=ProfileRepository().get_by_name('individual',symbol=symbol);signals=[];setups=[]
        evaluator=DailyBuySignalEvaluator()
        for index in range(60,len(prepared)):
            prefix=prepared.iloc[:index+1];row=prefix.iloc[-1]
            if not self._valid(row):continue
            trading_date=prefix.index[-1].date().isoformat();indicator=IndicatorResult(symbol=symbol,values={'rsi_14':float(row['rsi_14']),'sma_20':float(row['sma_20']),'ema_20':float(row['ema_20']),'macd':float(row['macd']),'bollinger_position':float(row['bollinger_position']),'adx_14':float(row['adx_14']),'stoch_k_14':float(row['stoch_k_14'])})
            signal=evaluator.evaluate(symbol,profile,self.ANALYSIS_PERIOD,trading_date,float(row['Close']),indicator);signals.append(signal)
            if signal.is_buy:
                outcome=evaluate_price_window(raw[['High','Low','Close']],trading_date,signal.entry_price,.08,60,1.0)
                setups.append(HistoricalSetupEntry(symbol,'individual',self.ANALYSIS_PERIOD,trading_date,signal.entry_price,.08,outcome.target_hit,outcome.days_to_target,outcome.max_gain_pct,outcome.max_drawdown_pct,outcome.window_start_date,outcome.window_end_date,outcome.window_end_return_pct,outcome.outcome.value,outcome.is_complete))
        DailyBuySignalRepository().replace_for(symbol,'individual',self.ANALYSIS_PERIOD,signals)
        setup_repo=HistoricalSetupRepository();setup_repo.delete_for(symbol,'individual',self.ANALYSIS_PERIOD)
        for setup in setups:setup_repo.upsert(setup)
        periods=RefreshBuyPeriodsUseCase().execute(symbol,'individual',self.ANALYSIS_PERIOD,3,.08)
        opportunities=HistoricalOpportunityReplayUseCase().execute(symbol,'individual',period=self.ANALYSIS_PERIOD)
        return IndividualHistoryBackfillResult(symbol,len(signals),sum(x.is_buy for x in signals),len(setups),len(periods),len(opportunities))
    def _prepare(self,data):
        p=data.copy();p['sma_20']=p['Close'].rolling(20).mean();p['ema_20']=p['Close'].ewm(span=20).mean();delta=p['Close'].diff();gain=delta.where(delta>0,0).rolling(14).mean();loss=-delta.where(delta<0,0).rolling(14).mean();p['rsi_14']=100-(100/(1+gain/loss));p['macd']=p['Close'].ewm(span=12).mean()-p['Close'].ewm(span=26).mean();mean=p['Close'].rolling(20).mean();std=p['Close'].rolling(20).std();p['bollinger_position']=(p['Close']-(mean-2*std))/(4*std);high,low,close=p['High'],p['Low'],p['Close'];up=high.diff();down=low.shift(1)-low;plus=up.where((up>down)&(up>0),0.0);minus=down.where((down>up)&(down>0),0.0);prev=close.shift(1);tr=pd.concat([high-low,(high-prev).abs(),(low-prev).abs()],axis=1).max(axis=1);atr=tr.rolling(14).mean();pdi=100*plus.rolling(14).mean()/atr;mdi=100*minus.rolling(14).mean()/atr;p['adx_14']=(100*(pdi-mdi).abs()/(pdi+mdi)).rolling(14).mean();lo=low.rolling(14).min();hi=high.rolling(14).max();p['stoch_k_14']=100*(close-lo)/(hi-lo);return p
    def _valid(self,row):return all(not pd.isna(row[c]) for c in ('Close','High','Low','rsi_14','sma_20','ema_20','macd','bollinger_position','adx_14','stoch_k_14'))
