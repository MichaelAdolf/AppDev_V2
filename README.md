from stockmind.domain.features.market_feature_snapshot import (
    MarketFeatureSnapshot
)

from stockmind.domain.rules.base_rule import (
    BaseRule
)

from stockmind.domain.rules.rule_result import (
    RuleResult
)


class TrendRule(
    BaseRule
):

    @property
    def name(self) -> str:
        return "trend"

    def evaluate(
        self,
        features: MarketFeatureSnapshot
    ) -> RuleResult:

        triggered = features.ema_above_sma

        return RuleResult(
            rule_name=self.name,
            triggered=triggered,
            score=20 if triggered else 0,
            reason=(
                "EMA liegt über SMA"
                if triggered
                else ""
            )
        )
