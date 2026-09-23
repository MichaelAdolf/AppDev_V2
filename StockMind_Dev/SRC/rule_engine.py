from stockmind.domain.rules.rule_set import ( RuleSet )

class RuleEngine:
    def __init__(
            self, 
            rule_set: RuleSet
    ):
        self._rule_set = rule_set

    def evaluate(self, features):
        results = []
        for rule in self._rule_set.rules:
            results.append(
                rule.evaluate(features)
            )
        return results