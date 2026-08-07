from stockmind.domain.confidence.confidence_result import (
    ConfidenceResult
)


class ConfidenceEngine:

    def calculate(
        self,
        rule_results
    ) -> ConfidenceResult:

        achieved_score = 0.0

        max_possible_score = 0.0

        for result in rule_results:

            achieved_score += result.score

            # Maximalscore der Regel:
            if result.rule_name == "rsi_oversold":
                max_possible_score += 15

            elif result.rule_name == "macd_positive":
                max_possible_score += 20

            elif result.rule_name == "trend":
                max_possible_score += 20

            elif result.rule_name == "lower_bollinger":
                max_possible_score += 25

        confidence = 0.0

        if max_possible_score > 0:

            confidence = (
                achieved_score
                / max_possible_score
            )

        return ConfidenceResult(
            confidence=confidence,
            achieved_score=achieved_score,
            max_possible_score=max_possible_score
        )
