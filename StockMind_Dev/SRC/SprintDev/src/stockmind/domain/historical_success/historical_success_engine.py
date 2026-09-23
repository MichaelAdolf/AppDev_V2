from datetime import timedelta

import pandas as pd

from stockmind.domain.core_setup.core_setup_engine import CoreSetupEngine
from stockmind.domain.features.feature_engine import FeatureEngine
from stockmind.domain.history.historical_outcome import (
    HistoricalOutcome,
    evaluate_price_window,
)
from stockmind.domain.historical_similarity.similarity_candidate import (
    SimilarityCandidate,
)
from stockmind.domain.historical_similarity.similarity_engine import SimilarityEngine
from stockmind.domain.historical_success.historical_success_result import (
    HistoricalSuccessResult,
)
from stockmind.domain.indicators.indicator_result import IndicatorResult
from stockmind.domain.profiles.trading_profile import TradingProfile
from stockmind.domain.quality.quality_engine import QualityEngine
from stockmind.domain.rules.rule_engine import RuleEngine
from stockmind.infrastructure.rules.rule_set_repository import RuleSetRepository


class HistoricalSuccessEngine:
    QUALITY_ORDER = {
        "LOW": 1,
        "MEDIUM": 2,
        "HIGH": 3,
        "VERY_HIGH": 4,
    }
    FLAT_THRESHOLD_PCT = 1.0

    def analyze(
        self,
        symbol: str,
        data: pd.DataFrame,
        profile: TradingProfile,
        rule_set_name: str = "entry_setup",
        target_pct: float = 0.08,
        lookahead_days: int = 60,
        min_quality: str = "MEDIUM",
        top_n_similar: int | None = None,
    ) -> HistoricalSuccessResult:
        prepared_data = self._prepare_data(data)
        rule_set = RuleSetRepository().get_by_name(rule_set_name)
        feature_engine = FeatureEngine()
        quality_engine = QualityEngine()
        core_setup_engine = CoreSetupEngine()
        similarity_engine = SimilarityEngine()

        current_features = self._build_current_features(
            symbol=symbol,
            prepared_data=prepared_data,
            profile=profile,
            feature_engine=feature_engine,
        )

        candidates: list[SimilarityCandidate] = []
        for index in range(30, len(prepared_data)):
            row = prepared_data.iloc[index]
            if not self._is_valid_setup_row(row):
                continue

            indicator_result = self._build_indicator_result(
                symbol=symbol,
                row=row,
            )
            features = feature_engine.build(
                result=indicator_result,
                profile=profile,
            )
            rule_results = RuleEngine(rule_set=rule_set).evaluate(features)
            core_setup_result = core_setup_engine.evaluate(rule_results)
            quality_result = quality_engine.calculate(
                rule_results=rule_results,
                core_setup_result=core_setup_result,
            )

            if not core_setup_result.setup_detected:
                continue
            if not self._meets_quality_threshold(
                quality=quality_result.quality,
                min_quality=min_quality,
            ):
                continue

            entry_price = float(row["Close"])
            evaluation = evaluate_price_window(
                data=prepared_data[["High", "Low", "Close"]],
                setup_date=row.name,
                entry_price=entry_price,
                target_pct=target_pct,
                lookahead_calendar_days=lookahead_days,
                flat_threshold_pct=self.FLAT_THRESHOLD_PCT,
            )
            similarity_score = similarity_engine.calculate(
                current=current_features,
                historical=features,
            )
            max_future_high = (
                entry_price * (1 + evaluation.max_gain_pct / 100)
                if evaluation.max_gain_pct is not None
                else entry_price
            )
            candidates.append(
                SimilarityCandidate(
                    trading_date=(
                        row.name.date()
                        if hasattr(row.name, "date")
                        else row.name
                    ),
                    similarity_score=similarity_score,
                    successful=(
                        evaluation.outcome == HistoricalOutcome.TARGET_HIT
                    ),
                    entry_price=entry_price,
                    max_future_high=max_future_high,
                    outcome=evaluation.outcome.value,
                    is_complete=evaluation.is_complete,
                    window_end_return_pct=evaluation.window_end_return_pct,
                    max_drawdown_pct=evaluation.max_drawdown_pct,
                    days_to_target=evaluation.days_to_target,
                )
            )

        selected_candidates = candidates
        if top_n_similar is not None:
            selected_candidates = sorted(
                candidates,
                key=lambda item: item.similarity_score,
                reverse=True,
            )[:top_n_similar]

        setup_count = len(selected_candidates)
        incomplete_count = sum(
            1
            for candidate in selected_candidates
            if candidate.outcome == HistoricalOutcome.INCOMPLETE_WINDOW.value
        )
        complete_candidates = [
            candidate
            for candidate in selected_candidates
            if candidate.outcome != HistoricalOutcome.INCOMPLETE_WINDOW.value
        ]
        complete_count = len(complete_candidates)

        target_hit_count = self._count_outcome(
            complete_candidates,
            HistoricalOutcome.TARGET_HIT,
        )
        below_target_count = self._count_outcome(
            complete_candidates,
            HistoricalOutcome.BELOW_TARGET,
        )
        flat_count = self._count_outcome(
            complete_candidates,
            HistoricalOutcome.FLAT,
        )
        negative_count = self._count_outcome(
            complete_candidates,
            HistoricalOutcome.NEGATIVE,
        )

        success_count = target_hit_count
        failure_count = complete_count - target_hit_count
        success_rate = self._rate(target_hit_count, complete_count)
        average_similarity = None
        if setup_count > 0:
            average_similarity = sum(
                candidate.similarity_score
                for candidate in selected_candidates
            ) / setup_count

        return HistoricalSuccessResult(
            symbol=symbol,
            profile_name=profile.name,
            rule_set_name=rule_set_name,
            setup_count=setup_count,
            success_count=success_count,
            failure_count=failure_count,
            success_rate=success_rate,
            target_pct=target_pct,
            lookahead_days=lookahead_days,
            min_quality=min_quality,
            sample_quality=self._sample_quality(complete_count),
            similarity_mode=top_n_similar is not None,
            top_n_similar=top_n_similar,
            average_similarity=average_similarity,
            complete_count=complete_count,
            target_hit_count=target_hit_count,
            below_target_count=below_target_count,
            flat_count=flat_count,
            negative_count=negative_count,
            incomplete_count=incomplete_count,
            target_hit_rate=self._rate(target_hit_count, complete_count),
            below_target_rate=self._rate(below_target_count, complete_count),
            flat_rate=self._rate(flat_count, complete_count),
            negative_rate=self._rate(negative_count, complete_count),
        )

    def _count_outcome(
        self,
        candidates: list[SimilarityCandidate],
        outcome: HistoricalOutcome,
    ) -> int:
        return sum(
            1 for candidate in candidates if candidate.outcome == outcome.value
        )

    def _rate(self, count: int, total: int) -> float:
        return count / total if total > 0 else 0.0

    def _build_current_features(
        self,
        symbol: str,
        prepared_data: pd.DataFrame,
        profile: TradingProfile,
        feature_engine: FeatureEngine,
    ):
        for index in range(len(prepared_data) - 1, 30, -1):
            row = prepared_data.iloc[index]
            if not self._is_valid_setup_row(row):
                continue
            indicator_result = self._build_indicator_result(
                symbol=symbol,
                row=row,
            )
            return feature_engine.build(
                result=indicator_result,
                profile=profile,
            )
        raise ValueError("No valid current feature row found.")

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

    def _meets_quality_threshold(self, quality: str, min_quality: str) -> bool:
        return self.QUALITY_ORDER.get(quality, 0) >= self.QUALITY_ORDER.get(
            min_quality,
            0,
        )

    def _prepare_data(self, data: pd.DataFrame) -> pd.DataFrame:
        prepared = data.copy()
        prepared.index = pd.to_datetime(prepared.index)
        if prepared.index.tz is not None:
            prepared.index = prepared.index.tz_localize(None)
        prepared = prepared.sort_index()
        prepared["sma_20"] = prepared["Close"].rolling(window=20).mean()
        prepared["ema_20"] = prepared["Close"].ewm(span=20).mean()
        prepared["rsi_14"] = self._calculate_rsi(prepared)
        prepared["macd"] = self._calculate_macd(prepared)
        prepared["bollinger_position"] = self._calculate_bollinger_position(
            prepared
        )
        prepared["adx_14"] = self._calculate_adx(prepared)
        prepared["stoch_k_14"] = self._calculate_stochastic(prepared)
        return prepared

    def _calculate_rsi(self, data: pd.DataFrame) -> pd.Series:
        delta = data["Close"].diff()
        gain = delta.where(delta > 0, 0).rolling(window=14).mean()
        loss = -delta.where(delta < 0, 0).rolling(window=14).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))

    def _calculate_macd(self, data: pd.DataFrame) -> pd.Series:
        ema12 = data["Close"].ewm(span=12).mean()
        ema26 = data["Close"].ewm(span=26).mean()
        return ema12 - ema26

    def _calculate_bollinger_position(self, data: pd.DataFrame) -> pd.Series:
        sma = data["Close"].rolling(window=20).mean()
        std = data["Close"].rolling(window=20).std()
        upper = sma + (std * 2)
        lower = sma - (std * 2)
        return (data["Close"] - lower) / (upper - lower)

    def _calculate_adx(self, data: pd.DataFrame) -> pd.Series:
        high = data["High"]
        low = data["Low"]
        close = data["Close"]
        up_move = high.diff()
        down_move = low.shift(1) - low
        plus_dm = up_move.where(
            (up_move > down_move) & (up_move > 0),
            0.0,
        )
        minus_dm = down_move.where(
            (down_move > up_move) & (down_move > 0),
            0.0,
        )
        previous_close = close.shift(1)
        true_range = pd.concat(
            [
                high - low,
                (high - previous_close).abs(),
                (low - previous_close).abs(),
            ],
            axis=1,
        ).max(axis=1)
        atr = true_range.rolling(window=14).mean()
        plus_di = 100 * (plus_dm.rolling(window=14).mean() / atr)
        minus_di = 100 * (minus_dm.rolling(window=14).mean() / atr)
        dx = 100 * ((plus_di - minus_di).abs() / (plus_di + minus_di))
        return dx.rolling(window=14).mean()

    def _calculate_stochastic(self, data: pd.DataFrame) -> pd.Series:
        low_14 = data["Low"].rolling(window=14).min()
        high_14 = data["High"].rolling(window=14).max()
        return 100 * ((data["Close"] - low_14) / (high_14 - low_14))

    def _is_valid_setup_row(self, row) -> bool:
        required_columns = [
            "rsi_14",
            "sma_20",
            "ema_20",
            "macd",
            "bollinger_position",
            "adx_14",
            "stoch_k_14",
            "Close",
            "High",
            "Low",
        ]
        return all(not pd.isna(row[column]) for column in required_columns)

    def _sample_quality(self, setup_count: int) -> str:
        if setup_count >= 50:
            return "HIGH"
        if setup_count >= 20:
            return "MEDIUM"
        if setup_count > 0:
            return "LOW"
        return "NO_SAMPLE"
