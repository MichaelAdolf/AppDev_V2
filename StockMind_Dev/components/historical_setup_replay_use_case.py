import pandas as pd
import yfinance as yf

from stockmind.application.history.daily_buy_signal_evaluator import (
    DailyBuySignalEvaluator,
)
from stockmind.domain.history.daily_buy_signal import DailyBuySignal
from stockmind.domain.history.historical_outcome import evaluate_price_window
from stockmind.domain.history.historical_setup_entry import HistoricalSetupEntry
from stockmind.domain.indicators.indicator_result import IndicatorResult
from stockmind.infrastructure.history.daily_buy_signal_repository import (
    DailyBuySignalRepository,
)
from stockmind.infrastructure.history.historical_setup_repository import (
    HistoricalSetupRepository,
)
from stockmind.infrastructure.profiles.profile_repository import ProfileRepository


class HistoricalSetupReplayUseCase:
    FLAT_THRESHOLD_PCT = 1.0

    def execute(
        self,
        symbol: str,
        profile_name: str,
        analysis_period: str,
        target_pct: float = 0.08,
        lookahead_days: int = 60,
        rule_set_name: str = "entry_setup",
        min_quality: str = "MEDIUM",
    ) -> list[HistoricalSetupEntry]:
        symbol = symbol.upper().strip()
        profile = ProfileRepository().get_by_name(profile_name)
        data = yf.Ticker(symbol).history(
            period=self._map_period(analysis_period)
        )
        print(symbol, len(data))
        if data.empty:
            DailyBuySignalRepository().replace_for(
                symbol=symbol,
                profile_name=profile_name,
                analysis_period=analysis_period,
                signals=[],
            )
            return []

        data = self._prepare_data(data)
        signals = self._evaluate_all_days(
            symbol=symbol,
            profile=profile,
            analysis_period=analysis_period,
            data=data,
            rule_set_name=rule_set_name,
            min_quality=min_quality,
        )
        DailyBuySignalRepository().replace_for(
            symbol=symbol,
            profile_name=profile_name,
            analysis_period=analysis_period,
            signals=signals,
        )

        entries = [
            self._evaluate_setup(
                signal=signal,
                data=data,
                target_pct=target_pct,
                lookahead_days=lookahead_days,
            )
            for signal in signals
            if signal.is_buy
        ]

        repository = HistoricalSetupRepository()
        repository.delete_for(
            symbol=symbol,
            profile_name=profile_name,
            analysis_period=analysis_period,
        )
        for entry in entries:
            repository.save(entry)
        return entries

    def _map_period(self, analysis_period: str) -> str:
        return {
            "1m": "1mo",
            "6m": "6mo",
            "1y": "1y",
            "3y": "3y",
            "5y": "5y",
        }.get(analysis_period, "1y")

    def _prepare_data(self, data: pd.DataFrame) -> pd.DataFrame:
        prepared = data.copy()
        prepared.index = pd.to_datetime(prepared.index)
        if prepared.index.tz is not None:
            prepared.index = prepared.index.tz_localize(None)
        prepared = prepared.sort_index()
        prepared["sma_20"] = prepared["Close"].rolling(20).mean()
        prepared["ema_20"] = prepared["Close"].ewm(span=20).mean()
        prepared["rsi_14"] = self._calculate_rsi(prepared)
        prepared["macd"] = self._calculate_macd(prepared)
        prepared["bollinger_position"] = self._calculate_bollinger_position(
            prepared
        )
        prepared["adx_14"] = self._calculate_adx(prepared)
        prepared["stoch_k_14"] = self._calculate_stochastic(prepared)
        return prepared

    def _evaluate_all_days(
        self,
        symbol,
        profile,
        analysis_period,
        data,
        rule_set_name,
        min_quality,
    ) -> list[DailyBuySignal]:
        evaluator = DailyBuySignalEvaluator()
        signals = []
        for index in range(30, len(data)):
            row = data.iloc[index]
            if not self._is_valid_indicator_row(row):
                continue
            indicator_result = self._build_indicator_result(symbol, row)
            signals.append(
                evaluator.evaluate(
                    symbol=symbol,
                    profile=profile,
                    analysis_period=analysis_period,
                    trading_date=row.name.date().isoformat(),
                    entry_price=float(row["Close"]),
                    indicator_result=indicator_result,
                    rule_set_name=rule_set_name,
                    min_quality=min_quality,
                )
            )
        return signals

    def _evaluate_setup(
        self,
        signal: DailyBuySignal,
        data: pd.DataFrame,
        target_pct: float,
        lookahead_days: int,
    ) -> HistoricalSetupEntry:
        evaluation = evaluate_price_window(
            data=data[["High", "Low", "Close"]],
            setup_date=signal.trading_date,
            entry_price=signal.entry_price,
            target_pct=target_pct,
            lookahead_calendar_days=lookahead_days,
            flat_threshold_pct=self.FLAT_THRESHOLD_PCT,
        )
        return HistoricalSetupEntry(
            symbol=signal.symbol,
            profile_name=signal.profile_name,
            analysis_period=signal.analysis_period,
            setup_date=signal.trading_date,
            entry_price=signal.entry_price,
            target_pct=target_pct,
            success=evaluation.target_hit,
            days_to_target=evaluation.days_to_target,
            max_gain_pct=evaluation.max_gain_pct,
            max_drawdown_pct=evaluation.max_drawdown_pct,
            window_start_date=evaluation.window_start_date,
            window_end_date=evaluation.window_end_date,
            window_end_return_pct=evaluation.window_end_return_pct,
            outcome=evaluation.outcome.value,
            is_complete=evaluation.is_complete,
        )

    def _build_indicator_result(self, symbol: str, row) -> IndicatorResult:
        return IndicatorResult(
            symbol=symbol,
            values={
                "rsi_14": float(row["rsi_14"]),
                "sma_20": float(row["sma_20"]),
                "ema_20": float(row["ema_20"]),
                "macd": float(row["macd"]),
                "bollinger_position": float(row["bollinger_position"]),
                "adx_14": float(row["adx_14"]),
                "stoch_k_14": float(row["stoch_k_14"]),
            },
        )

    def _is_valid_indicator_row(self, row) -> bool:
        required = [
            "Close", "High", "Low", "rsi_14", "sma_20", "ema_20",
            "macd", "bollinger_position", "adx_14", "stoch_k_14",
        ]
        return all(not pd.isna(row[column]) for column in required)

    def _calculate_rsi(self, data):
        delta = data["Close"].diff()
        gain = delta.where(delta > 0, 0).rolling(14).mean()
        loss = -delta.where(delta < 0, 0).rolling(14).mean()
        return 100 - (100 / (1 + gain / loss))

    def _calculate_macd(self, data):
        return data["Close"].ewm(span=12).mean() - data["Close"].ewm(
            span=26
        ).mean()

    def _calculate_bollinger_position(self, data):
        mean = data["Close"].rolling(20).mean()
        std = data["Close"].rolling(20).std()
        lower = mean - 2 * std
        upper = mean + 2 * std
        return (data["Close"] - lower) / (upper - lower)

    def _calculate_adx(self, data):
        high, low, close = data["High"], data["Low"], data["Close"]
        up_move = high.diff()
        down_move = low.shift(1) - low
        plus_dm = up_move.where((up_move > down_move) & (up_move > 0), 0.0)
        minus_dm = down_move.where((down_move > up_move) & (down_move > 0), 0.0)
        previous_close = close.shift(1)
        true_range = pd.concat(
            [high - low, (high - previous_close).abs(), (low - previous_close).abs()],
            axis=1,
        ).max(axis=1)
        atr = true_range.rolling(14).mean()
        plus_di = 100 * plus_dm.rolling(14).mean() / atr
        minus_di = 100 * minus_dm.rolling(14).mean() / atr
        dx = 100 * (plus_di - minus_di).abs() / (plus_di + minus_di)
        return dx.rolling(14).mean()

    def _calculate_stochastic(self, data):
        low_14 = data["Low"].rolling(14).min()
        high_14 = data["High"].rolling(14).max()
        return 100 * (data["Close"] - low_14) / (high_14 - low_14)
