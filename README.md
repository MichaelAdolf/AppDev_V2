from stockmind.domain.history.opportunity_trend_result import (
    OpportunityTrendResult
)


class OpportunityTrendEngine:

    def analyze(
        self,
        history
    ) -> OpportunityTrendResult:

        if not history:

            return OpportunityTrendResult(
                trend="NO_DATA",
                average_score=0.0,
                latest_score=0.0,
                score_change=0.0,
                history_size=0
            )

        scores = [
            item.opportunity_score
            for item in history
        ]

        average_score = (
            sum(scores)
            / len(scores)
        )

        latest_score = scores[-1]

        first_score = scores[0]

        score_change = (
            latest_score
            - first_score
        )

        if score_change >= 10:

            trend = "TRENDING_UP"

        elif score_change <= -10:

            trend = "TRENDING_DOWN"

        else:

            trend = "SIDEWAYS"

        return OpportunityTrendResult(
            trend=trend,
            average_score=average_score,
            latest_score=latest_score,
            score_change=score_change,
            history_size=len(scores)
        )
