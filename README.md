from stockmind.domain.features.market_feature_snapshot import (
    MarketFeatureSnapshot
)

from stockmind.domain.strategies.base_strategy import (
    BaseStrategy
)

from stockmind.domain.strategies.strategy_result import (
    StrategyResult
)


class TrendFollowingStrategy(
    BaseStrategy
):

    @property
    def name(self) -> str:
        return "trend_following"

    def evaluate(
        self,
        features: MarketFeatureSnapshot
    ) -> StrategyResult:

        score = 0.0

        reasons = []

        if features.ema_above_sma:

            score += 50

            reasons.append(
                "Aufwärtstrend erkannt"
            )

        if not features.is_overbought:

            score += 20

            reasons.append(
                "Nicht überkauft"
            )

        return StrategyResult(
            strategy_name=self.name,
            score=score,
            reasons=reasons
        )
