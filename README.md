import pandas as pd

from stockmind.domain.historical_success.historical_success_result import (
    HistoricalSuccessResult
)

from stockmind.domain.historical_similarity.similarity_candidate import (
    SimilarityCandidate
)

from stockmind.domain.historical_similarity.similarity_engine import (
    SimilarityEngine
)

from stockmind.domain.indicators.indicator_result import (
    IndicatorResult
)

from stockmind.domain.features.feature_engine import (
    FeatureEngine
)

from stockmind.domain.rules.rule_engine import (
    RuleEngine
)

from stockmind.domain.quality.quality_engine import (
    QualityEngine
)

from stockmind.domain.core_setup.core_setup_engine import (
    CoreSetupEngine
)

from stockmind.domain.profiles.trading_profile import (
    TradingProfile
)

from stockmind.infrastructure.rules.rule_set_repository import (
    RuleSetRepository
)


class HistoricalSuccessEngine:

    QUALITY_ORDER = {
        "LOW": 1,
        "MEDIUM": 2,
        "HIGH": 3,
        "VERY_HIGH": 4,
    }

    def analyze(
        self,
        symbol: str,
        data: pd.DataFrame,
        profile: TradingProfile,
        rule_set_name: str = "entry_setup",
        target_pct: float = 0.08,
        lookahead_days: int = 60,
        min_quality: str = "MEDIUM",
        top_n_similar: int | None = None
    ) -> HistoricalSuccessResult:

        prepared_data = self._prepare_data(
            data
        )

        rule_set = (
            RuleSetRepository()
            .get_by_name(
                rule_set_name
            )
        )

        feature_engine = FeatureEngine()

        quality_engine = QualityEngine()

        core_setup_engine = CoreSetupEngine()

        similarity_engine = SimilarityEngine()

        current_features = self._build_current_features(
            symbol=symbol,
            prepared_data=prepared_data,
            profile=profile,
            feature_engine=feature_engine
        )

        candidates = []

        max_index = (
            len(prepared_data)
            - lookahead_days
            - 1
        )

        for index in range(
            30,
            max_index
        ):

            row = prepared_data.iloc[
                index
            ]

            if not self._is_valid_setup_row(
                row
            ):

                continue

            indicator_result = self._build_indicator_result(
                symbol=symbol,
                row=row
            )

            features = feature_engine.build(
                result=indicator_result,
                profile=profile
            )

            rule_engine = RuleEngine(
                rule_set=rule_set
            )

            rule_results = rule_engine.evaluate(
                features
            )

            core_setup_result = (
                core_setup_engine.evaluate(
                    rule_results
                )
            )

            quality_result = quality_engine.calculate(
                rule_results=rule_results,
                core_setup_result=core_setup_result
            )

            if not core_setup_result.setup_detected:

                continue

            if not self._meets_quality_threshold(
                quality=quality_result.quality,
                min_quality=min_quality
            ):

                continue

            entry_price = float(
                row["Close"]
            )

            target_price = entry_price * (
                1 + target_pct
            )

            future_window = prepared_data.iloc[
                index + 1:
                index + 1 + lookahead_days
            ]

            max_future_high = float(
                future_window["High"].max()
            )

            successful = (
                max_future_high
                >= target_price
            )

            similarity_score = similarity_engine.calculate(
                current=current_features,
                historical=features
            )

            candidates.append(
                SimilarityCandidate(
                    trading_date=row.name.date()
                    if hasattr(row.name, "date")
                    else row.name,
                    similarity_score=similarity_score,
                    successful=successful,
                    entry_price=entry_price,
                    max_future_high=max_future_high
                )
            )

        selected_candidates = candidates

        if top_n_similar is not None:

            selected_candidates = sorted(
                candidates,
                key=lambda item: item.similarity_score,
                reverse=True
            )[:top_n_similar]

        setup_count = len(
            selected_candidates
        )

        success_count = sum(
            1
            for candidate in selected_candidates
            if candidate.successful
        )

        failure_count = (
            setup_count
            - success_count
        )

        success_rate = 0.0

        if setup_count > 0:

            success_rate = (
                success_count
                / setup_count
            )

        average_similarity = None

        if setup_count > 0:

            average_similarity = (
                sum(
                    candidate.similarity_score
                    for candidate in selected_candidates
                )
                / setup_count
            )

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
            sample_quality=self._sample_quality(
                setup_count
            ),
            similarity_mode=top_n_similar is not None,
            top_n_similar=top_n_similar,
            average_similarity=average_similarity
        )

    def _build_current_features(
        self,
        symbol: str,
        prepared_data: pd.DataFrame,
        profile: TradingProfile,
        feature_engine: FeatureEngine
    ):

        for index in range(
            len(prepared_data) - 1,
            30,
            -1
        ):

            row = prepared_data.iloc[
                index
            ]

            if not self._is_valid_setup_row(
                row
            ):

                continue

            indicator_result = self._build_indicator_result(
                symbol=symbol,
                row=row
            )

            return feature_engine.build(
                result=indicator_result,
                profile=profile
            )

        raise ValueError(
            "No valid current feature row found."
        )

    def _build_indicator_result(
        self,
        symbol: str,
        row
    ) -> IndicatorResult:

        return IndicatorResult(
            symbol=symbol,
            values={
                "rsi_14": float(
                    row["rsi_14"]
                ),
                "sma_20": float(
                    row["sma_20"]
                ),
                "ema_20": float(
                    row["ema_20"]
                ),
                "macd": float(
                    row["macd"]
                ),
                "bollinger_position": float(
                    row["bollinger_position"]
                ),
                "adx_14": float(
                    row["adx_14"]
                ),
                "stoch_k_14": float(
                    row["stoch_k_14"]
                ),
            }
        )

    def _meets_quality_threshold(
        self,
        quality: str,
        min_quality: str
    ) -> bool:

        return (
            self.QUALITY_ORDER.get(
                quality,
                0
            )
            >=
            self.QUALITY_ORDER.get(
                min_quality,
                0
            )
        )

    def _prepare_data(
        self,
        data: pd.DataFrame
    ) -> pd.DataFrame:

        prepared = data.copy()

        prepared["sma_20"] = (
            prepared["Close"]
            .rolling(
                window=20
            )
            .mean()
        )

        prepared["ema_20"] = (
            prepared["Close"]
            .ewm(
                span=20
            )
            .mean()
        )

        prepared["rsi_14"] = self._calculate_rsi(
            prepared
        )

        prepared["macd"] = self._calculate_macd(
            prepared
        )

        prepared["bollinger_position"] = (
            self._calculate_bollinger_position(
                prepared
            )
        )

        prepared["adx_14"] = self._calculate_adx(
            prepared
        )

        prepared["stoch_k_14"] = (
            self._calculate_stochastic(
                prepared
            )
        )

        return prepared

    def _calculate_rsi(
        self,
        data: pd.DataFrame
    ) -> pd.Series:

        delta = data["Close"].diff()

        gain = (
            delta.where(
                delta > 0,
                0
            )
            .rolling(
                window=14
            )
            .mean()
        )

        loss = (
            -delta.where(
                delta < 0,
                0
            )
            .rolling(
                window=14
            )
            .mean()
        )

        rs = gain / loss

        rsi = 100 - (
            100 / (1 + rs)
        )

        return rsi

    def _calculate_macd(
        self,
        data: pd.DataFrame
    ) -> pd.Series:

        ema12 = (
            data["Close"]
            .ewm(
                span=12
            )
            .mean()
        )

        ema26 = (
            data["Close"]
            .ewm(
                span=26
            )
            .mean()
        )

        return ema12 - ema26

    def _calculate_bollinger_position(
        self,
        data: pd.DataFrame
    ) -> pd.Series:

        sma = (
            data["Close"]
            .rolling(
                window=20
            )
            .mean()
        )

        std = (
            data["Close"]
            .rolling(
                window=20
            )
            .std()
        )

        upper = sma + (
            std * 2
        )

        lower = sma - (
            std * 2
        )

        position = (
            data["Close"] - lower
        ) / (
            upper - lower
        )

        return position

    def _calculate_adx(
        self,
        data: pd.DataFrame
    ) -> pd.Series:

        high = data["High"]

        low = data["Low"]

        close = data["Close"]

        up_move = high.diff()

        down_move = (
            low.shift(1)
            - low
        )

        plus_dm = up_move.where(
            (up_move > down_move)
            & (up_move > 0),
            0.0
        )

        minus_dm = down_move.where(
            (down_move > up_move)
            & (down_move > 0),
            0.0
        )

        previous_close = close.shift(1)

        true_range = pd.concat(
            [
                high - low,
                (
                    high
                    - previous_close
                ).abs(),
                (
                    low
                    - previous_close
                ).abs(),
            ],
            axis=1
        ).max(
            axis=1
        )

        atr = (
            true_range
            .rolling(
                window=14
            )
            .mean()
        )

        plus_di = 100 * (
            plus_dm.rolling(
                window=14
            ).mean()
            / atr
        )

        minus_di = 100 * (
            minus_dm.rolling(
                window=14
            ).mean()
            / atr
        )

        dx = 100 * (
            (
                plus_di
                - minus_di
            ).abs()
            / (
                plus_di
                + minus_di
            )
        )

        adx = (
            dx
            .rolling(
                window=14
            )
            .mean()
        )

        return adx

    def _calculate_stochastic(
        self,
        data: pd.DataFrame
    ) -> pd.Series:

        low_14 = (
            data["Low"]
            .rolling(
                window=14
            )
            .min()
        )

        high_14 = (
            data["High"]
            .rolling(
                window=14
            )
            .max()
        )

        stoch_k = 100 * (
            (
                data["Close"]
                - low_14
            )
            / (
                high_14
                - low_14
            )
        )

        return stoch_k

    def _is_valid_setup_row(
        self,
        row
    ) -> bool:

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
        ]

        for column in required_columns:

            if pd.isna(
                row[column]
            ):

                return False

        return True

    def _sample_quality(
        self,
        setup_count: int
    ) -> str:

        if setup_count >= 50:

            return "HIGH"

        if setup_count >= 20:

            return "MEDIUM"

        if setup_count > 0:

            return "LOW"

        return "NO_SAMPLE"
