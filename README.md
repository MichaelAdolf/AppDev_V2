from stockmind.domain.features.market_feature_snapshot import (
    MarketFeatureSnapshot
)


class SimilarityEngine:

    def calculate(
        self,
        current: MarketFeatureSnapshot,
        historical: MarketFeatureSnapshot
    ) -> float:

        distances = []

        # RSI: 0 bis 100
        distances.append(
            self._normalized_distance(
                current.rsi,
                historical.rsi,
                scale=100
            )
        )

        # Bollinger Position: typischer Bereich 0 bis 1
        distances.append(
            self._normalized_distance(
                current.bollinger_position,
                historical.bollinger_position,
                scale=1
            )
        )

        # ADX: 0 bis 100
        if (
            current.adx_14 is not None
            and historical.adx_14 is not None
        ):

            distances.append(
                self._normalized_distance(
                    current.adx_14,
                    historical.adx_14,
                    scale=100
                )
            )

        # Stochastic: 0 bis 100
        if (
            current.stoch_k_14 is not None
            and historical.stoch_k_14 is not None
        ):

            distances.append(
                self._normalized_distance(
                    current.stoch_k_14,
                    historical.stoch_k_14,
                    scale=100
                )
            )

        if not distances:

            return 0.0

        average_distance = (
            sum(distances)
            / len(distances)
        )

        similarity = (
            1.0
            - average_distance
        )

        return max(
            0.0,
            min(
                1.0,
                similarity
            )
        )

    def _normalized_distance(
        self,
        value_a: float,
        value_b: float,
        scale: float
    ) -> float:

        if scale <= 0:

            return 1.0

        distance = abs(
            value_a
            - value_b
        ) / scale

        return max(
            0.0,
            min(
                1.0,
                distance
            )
        )
