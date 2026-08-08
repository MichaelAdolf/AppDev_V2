from stockmind.domain.features.market_feature_snapshot import (
    MarketFeatureSnapshot
)

from stockmind.domain.rules.base_rule import (
    BaseRule
)

from stockmind.domain.rules.rule_result import (
    RuleResult
)


class StochasticOversoldRule(
    BaseRule
):

    @property
    def name(self) -> str:
        return "stochastic_oversold"

    def evaluate(
        self,
        features: MarketFeatureSnapshot
    ) -> RuleResult:

        triggered = features.stoch_oversold

        return RuleResult(
            rule_name=self.name,
            triggered=triggered,
            score=10 if triggered else 0,
            reason=(
                "Stochastic befindet sich im überverkauften Bereich"
                if triggered
                else ""
            )
        )
