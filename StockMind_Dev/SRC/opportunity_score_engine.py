from stockmind.domain.scoring.opportunity_score_result import OpportunityScoreResult


class OpportunityScoreEngine:
    QUALITY_POINTS = {
        "LOW": 25,
        "MEDIUM": 50,
        "HIGH": 75,
        "VERY_HIGH": 100,
    }
    RISK_PENALTY = {
        "LOW": 0,
        "MEDIUM": 15,
        "HIGH": 30,
    }

    def calculate(
        self,
        quality_result,
        confidence_result,
        historical_success_result,
        risk_result,
        profile,
    ) -> OpportunityScoreResult:
        quality_points = self.QUALITY_POINTS.get(quality_result.quality, 0)
        weights = profile.opportunity_profile
        historical_rate = historical_success_result.success_rate
        historical_source = getattr(
            historical_success_result,
            "source",
            "SETUPS",
        )

        quality_component = quality_points * weights.quality_weight
        confidence_component = (
            confidence_result.confidence * 100 * weights.confidence_weight
        )
        historical_component = (
            historical_rate * 100 * weights.historical_weight
        )
        risk_penalty = self.RISK_PENALTY.get(risk_result.level, 0)
        risk_component = risk_penalty * -weights.risk_weight
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
            risk_component=risk_component,
            historical_rate=historical_rate,
            historical_source=historical_source,
        )
