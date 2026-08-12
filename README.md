from stockmind.domain.explainability.explanation_result import (
    ExplanationResult
)


class ExplanationEngine:

    def create(
        self,
        symbol: str,
        core_setup_result,
        quality_result,
        confidence_result,
        historical_result,
        risk_result,
        opportunity_result,
        rule_results
    ) -> ExplanationResult:

        strengths = []

        weaknesses = []

        for result in rule_results:

            if result.triggered:

                strengths.append(
                    result.reason
                )

            else:

                weaknesses.append(
                    result.rule_name
                )

        strengths.append(
            (
                f"Historische Erfolgsrate "
                f"{historical_result.success_rate:.1%}"
            )
        )

        if (
            historical_result.average_similarity
            is not None
        ):

            strengths.append(
                (
                    f"Durchschnittliche Ähnlichkeit "
                    f"{historical_result.average_similarity:.2f}"
                )
            )

        summary = (
            f"{symbol}: "
            f"{quality_result.quality} Setup, "
            f"Confidence "
            f"{confidence_result.confidence:.1%}, "
            f"Risk "
            f"{risk_result.level}"
        )

        return ExplanationResult(
            title=f"{symbol} Analyse",
            summary=summary,
            strengths=strengths,
            weaknesses=weaknesses,
            opportunity_score=(
                opportunity_result.score
            )
        )
