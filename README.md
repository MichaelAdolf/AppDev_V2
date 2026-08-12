from stockmind.domain.scoring.opportunity_score_result import (
    OpportunityScoreResult
)


class OpportunityScoreEngine:

    QUALITY_POINTS = {
        "LOW": 25,
        "MEDIUM": 50,
        "HIGH": 75,
        "VERY_HIGH": 100
    }

    RISK_PENALTY = {
        "LOW": 0,
        "MEDIUM": 15,
        "HIGH": 30
    }

    def calculate(
        self,
        quality_result,
        confidence_result,
        historical_success_result,
        risk_result
    ) -> OpportunityScoreResult:

        quality_points = self.QUALITY_POINTS.get(
            quality_result.quality,
            0
        )

        quality_component = (
            quality_points * 0.30
        )

        confidence_component = (
            confidence_result.confidence
            * 100
            * 0.40
        )

        historical_component = (
            historical_success_result.success_rate
            * 100
            * 0.20
        )

        risk_penalty = (
            self.RISK_PENALTY.get(
                risk_result.level,
                0
            )
        )

        risk_component = (
            risk_penalty * -0.10
        )

        score = (
            quality_component
            + confidence_component
            + historical_component
            + risk_component
        )

        return OpportunityScoreResult(
            score=score,
            quality_component=quality_component,
            confidence_component=confidence_component,
            historical_component=historical_component,
            risk_component=risk_component
        )
