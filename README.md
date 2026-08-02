from stockmind.domain.rules.rule_set import (
    RuleSet
)

from stockmind.domain.rules.rsi_oversold_rule import (
    RSIOversoldRule
)

from stockmind.domain.rules.lower_bollinger_rule import (
    LowerBollingerRule
)

from stockmind.domain.rules.trend_rule import (
    TrendRule
)

from stockmind.domain.rules.macd_positive_rule import (
    MACDPositiveRule
)


class RuleSetRepository:
    """
    Zentrale Quelle für alle aktuell verfügbaren RuleSets.

    Aktuell sind die RuleSets noch fest in Python definiert.
    Später können sie aus YAML oder JSON geladen werden.
    """

    def get_by_name(
        self,
        name: str
    ) -> RuleSet:

        if name == "mean_reversion":

            return self._get_mean_reversion_rule_set()

        if name == "trend_following":

            return self._get_trend_following_rule_set()

        raise ValueError(
            f"Unknown rule set: {name}"
        )

    def get_all(
        self
    ) -> listreturn [
            self._get_mean_reversion_rule_set(),
            self._get_trend_following_rule_set(),
        ]

    def _get_mean_reversion_rule_set(
        self
    ) -> RuleSet:

        return RuleSet(
            name="mean_reversion",
            rules=[
                RSIOversoldRule(),
                LowerBollingerRule(),
            ]
        )

    def _get_trend_following_rule_set(
        self
    ) -> RuleSet:

        return RuleSet(
            name="trend_following",
            rules=[
                TrendRule(),
                MACDPositiveRule(),
            ]
        )
