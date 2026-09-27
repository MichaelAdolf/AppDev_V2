from dataclasses import dataclass


@dataclass(frozen=True)
class DailyIntelligenceItem:
    symbol: str
    company_name: str
    profile_name: str
    current_score: float
    previous_score: float | None
    score_change: float | None
    current_confidence: float
    confidence_change: float | None
    current_signal: str
    previous_signal: str | None
    signal_changed: bool
    current_risk: str
    previous_risk: str | None
    active_period_start: str | None
    active_period_duration_days: int | None
    new_buy_period: bool
    target_hit_rate: float
    complete_period_count: int
    sample_quality: str
    profile_buy_count: int
    profile_consensus: str
    relevance_status: str
    relevance_priority: int


@dataclass(frozen=True)
class DailyIntelligenceResult:
    profile_name: str
    latest_trading_date: str | None
    previous_trading_date: str | None
    stock_count: int
    relevant_count: int
    new_buy_period_count: int
    signal_change_count: int
    consensus_count: int
    score_gainer_count: int
    items: list[DailyIntelligenceItem]
