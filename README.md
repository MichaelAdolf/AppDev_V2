from stockmind.domain.quality.quality_result import (
    QualityResult
)


class QualityEngine:

    CONFIRMATION_RULES = [
        "stochastic_oversold",
        "macd_positive",
        "trend",
    ]

    def calculate(
        self,
        rule_results,
        core_setup_result=None
    ) -> QualityResult:

        total_score = 0.0

        reasons = []

        for result in rule_results:

            total_score += result.score

            if result.reason:

                reasons.append(
                    result.reason
                )

        if core_setup_result is None:

            return self._calculate_legacy_quality(
                total_score=total_score,
                reasons=reasons
            )

        if not core_setup_result.setup_detected:

            missing = ", ".join(
                core_setup_result.missing_rules
            )

            return QualityResult(
                quality="LOW",
                score=total_score,
                reasons=[
                    *reasons,
                    (
                        "Core Setup nicht vollständig erfüllt: "
                        f"{missing}"
                    )
                ]
            )

        confirmation_score = 0.0

        for result in rule_results:

            if result.rule_name in self.CONFIRMATION_RULES:

                confirmation_score += result.score

        if confirmation_score >= 40:

            quality = "VERY_HIGH"

        elif confirmation_score >= 20:

            quality = "HIGH"

        elif confirmation_score >= 10:

            quality = "MEDIUM"

        else:

            quality = "MEDIUM"

        return QualityResult(
            quality=quality,
            score=total_score,
            reasons=reasons
        )

    def _calculate_legacy_quality(
        self,
        total_score: float,
        reasons: list[str]
    ) -> QualityResult:

        if total_score >= 75:

            quality = "VERY_HIGH"

        elif total_score >= 50:

            quality = "HIGH"

        elif total_score >= 25:

            quality = "MEDIUM"

        else:

            quality = "LOW"

        return QualityResult(
            quality=quality,
            score=total_score,
            reasons=reasons
        )
