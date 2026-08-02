from stockmind.domain.features.market_feature_snapshot import (
    MarketFeatureSnapshot
)

from stockmind.domain.strategies.base_strategy import (
    BaseStrategy
)

from stockmind.domain.strategies.strategy_result import (
    StrategyResult
)


class MeanReversionStrategy(
    BaseStrategy
):

    @property
    def name(self) -> str:
        return "mean_reversion"

    def evaluate(
        self,
        features: MarketFeatureSnapshot
    ) -> StrategyResult:

        score = 0.0

        reasons = []

        if features.is_oversold:

            score += 40

            reasons.append(
                "RSI überverkauft"
            )

        if features.ema_above_sma:

            score += 20

            reasons.append(
                "EMA über SMA"
            )

        return StrategyResult(
            strategy_name=self.name,
            score=score,
            reasons=reasons
        )
