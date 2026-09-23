from datetime import datetime

from stockmind.domain.enums.signal_type import (
    SignalType
)

from stockmind.domain.scoring.score_result import (
    ScoreResult
)

from stockmind.domain.value_objects.signal_decision import (
    SignalDecision
)

class SignalEngine:
    
    def create_signal(
        self,
        symbol: str,
        quality_result,
        confidence_result,
        risk_result
    ) -> SignalDecision:

        quality = quality_result.quality

        confidence = (confidence_result.confidence)

        risk_level = (risk_result.level)

        if (
            quality in ["VERY_HIGH", "HIGH"]
            and confidence >= 0.6
            and risk_level != "HIGH"
        ):
            signal = SignalType.BUY

        elif quality == "LOW":
            signal = SignalType.SELL

        else:
            signal = SignalType.HOLD

        reasons = []

        reasons.extend(quality_result.reasons)

        reasons.extend(risk_result.reasons)

        return SignalDecision(
            symbol=symbol,
            signal=signal,
            quality=quality,
            confidence=confidence,
            risk_level=risk_level,
            reasons=reasons,
            created_at=datetime.now()
        )