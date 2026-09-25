from dataclasses import dataclass


@dataclass(frozen=True)
class OpportunityScoreResult:
    score: float
    quality_component: float
    confidence_component: float
    historical_component: float
    risk_component: float
    historical_rate: float = 0.0
    historical_source: str = "UNKNOWN"
