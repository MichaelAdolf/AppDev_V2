from dataclasses import dataclass

@dataclass(frozen=True)
class AnalysisHistoryEntry:
    analysis_date: str

    symbol: str

    profile_name: str

    opportunity_score: float

    confidence: float

    historical_success_rate: float

    risk_level: str

    signal: str