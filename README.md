from stockmind.domain.features.market_feature_snapshot import (
    MarketFeatureSnapshot
)

from stockmind.domain.rules.base_rule import (
    BaseRule
)

from stockmind.domain.rules.rule_result import (
    RuleResult
)


class RSIOversoldRule(
    BaseRule
):

    @property
    def name(self) -> str:
        return "rsi_oversold"

    def evaluate(
        self,
        features: MarketFeatureSnapshot
    ) -> RuleResult:

        triggered = features.is_oversold

        return RuleResult(
            rule_name=self.name,

            triggered=triggered,

            score=15 if triggered else 0,

            reason=(
                "RSI liegt im überverkauften Bereich"
                if triggered
                else ""
            )
        )
