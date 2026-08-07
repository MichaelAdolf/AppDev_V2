from stockmind.domain.quality.quality_result import (
    QualityResult
)


class QualityEngine:

    def calculate(
        self,
        rule_results
    ) -> QualityResult:

        total_score = 0.0

        reasons = []

        for result in rule_results:

            total_score += result.score

            if result.reason:

                reasons.append(
                    result.reason
                )

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
