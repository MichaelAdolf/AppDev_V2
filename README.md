from stockmind.domain.confidence.confidence_result import (
    ConfidenceResult
)


class ConfidenceEngine:

    RULE_MAX_SCORES = {
        "rsi_oversold": 15,
        "macd_positive": 20,
        "trend": 20,
        "lower_bollinger": 25,
        "adx_strength": 15,
        "stochastic_oversold": 10,
    }

    HISTORICAL_WEIGHT_BY_SAMPLE_QUALITY = {
        "HIGH": 0.70,
        "MEDIUM": 0.60,
        "LOW": 0.40,
        "NO_SAMPLE": 0.0,
    }

    def calculate(
        self,
        rule_results,
        historical_success_result=None
    ) -> ConfidenceResult:

        achieved_score = 0.0

        max_possible_score = 0.0

        for result in rule_results:

            achieved_score += result.score

            max_possible_score += (
                self.RULE_MAX_SCORES.get(
                    result.rule_name,
                    0
                )
            )

        rule_confidence = 0.0

        if max_possible_score > 0:

            rule_confidence = (
                achieved_score
                / max_possible_score
            )

        if historical_success_result is None:

            return ConfidenceResult(
                confidence=rule_confidence,
                achieved_score=achieved_score,
                max_possible_score=max_possible_score,
                rule_confidence=rule_confidence,
                historical_success_rate=None,
                source="RULES",
                sample_quality=None
            )

        historical_success_rate = (
            historical_success_result.success_rate
        )

        sample_quality = (
            historical_success_result.sample_quality
        )

        historical_weight = (
            self.HISTORICAL_WEIGHT_BY_SAMPLE_QUALITY.get(
                sample_quality,
                0.0
            )
        )

        rule_weight = (
            1.0
            - historical_weight
        )

        combined_confidence = (
            historical_success_rate
            * historical_weight
            +
            rule_confidence
            * rule_weight
        )

        if historical_weight == 0.0:

            source = "RULES"

        elif historical_weight >= 0.6:

            source = "HISTORICAL"

        else:

            source = "HYBRID"

        return ConfidenceResult(
            confidence=combined_confidence,
            achieved_score=achieved_score,
            max_possible_score=max_possible_score,
            rule_confidence=rule_confidence,
            historical_success_rate=historical_success_rate,
            source=source,
            sample_quality=sample_quality
        )
