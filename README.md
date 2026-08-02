from stockmind.domain.scoring.score_result import (
    ScoreResult
)


class ScoringEngine:

    def calculate(
        self,
        strategy_results
    ) -> ScoreResult:

        total_score = 0.0

        reasons = []

        for result in strategy_results:

            total_score += result.score

            reasons.extend(
                result.reasons
            )

        return ScoreResult(
            total_score=total_score,
            reasons=reasons
        )
