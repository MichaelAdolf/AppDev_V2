from dataclasses import dataclass


@dataclass(frozen=True)
class HistoricalOpportunityEntry:
    symbol: str
    profile_name: str
    trading_date: str
    opportunity_score: float
    confidence: float
    historical_success_rate: float
    historical_sample_count: int
    historical_source: str
    risk_level: str
    signal: str
    quality: str
