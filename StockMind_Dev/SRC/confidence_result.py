from dataclasses import dataclass

@dataclass(frozen=True)
class ConfidenceResult:
    confidence: float
    achieved_score: float
    max_possible_score: float
    rule_confidence: float
    historical_success_rate: float | None = None
    source: str = "RULES"
    sample_quality: str | None = None