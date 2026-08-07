from stockmind.domain.value_objects.market_feature_snapshot import (
    MarketFeatureSnapshot
)

from stockmind.domain.rules.base_rule import (
    BaseRule
)

from stockmind.domain.rules.rule_result import (
    RuleResult
)


class ADXStrengthRule(
    BaseRule
):

    @property
    def name(self) -> str:
        return "adx_strength"

    def evaluate(
        self,
        features: MarketFeatureSnapshot
    ) -> RuleResult:

        triggered = features.adx_trend_strength

        return RuleResult(
            rule_name=self.name,
            triggered=triggered,
            score=15 if triggered else 0,
            reason=(
                "ADX zeigt ausreichende Bewegungsstärke"
                if triggered
                else ""
            )
        )
