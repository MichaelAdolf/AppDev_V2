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
    quality_component: float
    confidence_component: float
    historical_component: float
    risk_component: float
    outcome: str
    is_complete: bool
    days_to_target: int | None
    max_gain_pct: float | None
    max_drawdown_pct: float | None
