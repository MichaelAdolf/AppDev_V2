from dataclasses import dataclass

@dataclass(frozen=True)
class OpportunityScoreProfile:

    name: str

    quality_weight: float

    confidence_weight: float

    historical_weight: float

    risk_weight: float