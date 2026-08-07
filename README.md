from stockmind.domain.risk.risk_result import (
    RiskResult
)


class RiskEngine:

    def calculate(
        self,
        features
    ) -> RiskResult:

        risk_score = 0

        reasons = []

        if features.is_overbought:

            risk_score += 50

            reasons.append(
                "Markt wirkt überkauft"
            )

        if not features.ema_above_sma:

            risk_score += 30

            reasons.append(
                "Schwacher Trend"
            )

        if features.near_lower_bollinger:

            risk_score += 20

            reasons.append(
                "Nahe unterem Bollinger-Band"
            )

        if risk_score >= 70:

            level = "HIGH"

        elif risk_score >= 40:

            level = "MEDIUM"

        else:

            level = "LOW"

        return RiskResult(
            level=level,
            score=risk_score,
            reasons=reasons
        )
