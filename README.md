from stockmind.domain.core_setup.core_setup_result import (
    CoreSetupResult
)


class CoreSetupEngine:

    REQUIRED_RULES = [
        "rsi_oversold",
        "lower_bollinger",
        "adx_strength",
    ]

    def evaluate(
        self,
        rule_results
    ) -> CoreSetupResult:

        results_by_name = {
            result.rule_name: result
            for result in rule_results
        }

        satisfied_rules = 0

        core_score = 0.0

        missing_rules = []

        reasons = []

        for rule_name in self.REQUIRED_RULES:

            result = results_by_name.get(
                rule_name
            )

            if result is None:

                missing_rules.append(
                    rule_name
                )

                continue

            if result.triggered:

                satisfied_rules += 1

                core_score += result.score

                if result.reason:

                    reasons.append(
                        result.reason
                    )

            else:

                missing_rules.append(
                    rule_name
                )

        setup_detected = (
            satisfied_rules
            == len(
                self.REQUIRED_RULES
            )
        )

        return CoreSetupResult(
            setup_detected=setup_detected,
            satisfied_rules=satisfied_rules,
            required_rules=len(
                self.REQUIRED_RULES
            ),
            core_score=core_score,
            missing_rules=missing_rules,
            reasons=reasons
        )
