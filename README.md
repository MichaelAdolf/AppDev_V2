from stockmind.domain.features.market_feature_snapshot import (
    MarketFeatureSnapshot
)

from stockmind.domain.rules.base_rule import (
    BaseRule
)

from stockmind.domain.rules.rule_result import (
    RuleResult
)


class LowerBollingerRule(
    BaseRule
):

    @property
    def name(self) -> str:
        return "lower_bollinger"

    def evaluate(
        self,
        features: MarketFeatureSnapshot
    ) -> RuleResult:

        triggered = features.near_lower_bollinger

        return RuleResult(
            rule_name=self.name,
            triggered=triggered,
            score=25 if triggered else 0,
            reason=(
                "Nahe unterem Bollinger-Band"
                if triggered
                else ""
            )
        )
