from stockmind.domain.features.market_feature_snapshot import (
    MarketFeatureSnapshot
)

from stockmind.domain.rules.base_rule import (
    BaseRule
)

from stockmind.domain.rules.rule_result import (
    RuleResult
)


class MACDPositiveRule(
    BaseRule
):

    @property
    def name(self) -> str:
        return "macd_positive"

    def evaluate(
        self,
        features: MarketFeatureSnapshot
    ) -> RuleResult:

        triggered = features.macd_positive

        return RuleResult(
            rule_name=self.name,
            triggered=triggered,
            score=20 if triggered else 0,
            reason=(
                "MACD ist positiv"
                if triggered
                else ""
            )
        )
