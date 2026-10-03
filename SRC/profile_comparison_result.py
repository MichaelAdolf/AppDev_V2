from dataclasses import dataclass


@dataclass(frozen=True)
class ProfileComparisonEntry:
    profile_name: str
    score: float
    confidence: float
    signal: str
    risk_level: str
    current_buy_signal: bool | None
    active_period_start: str | None
    active_period_duration_days: int | None
    period_count: int
    complete_period_count: int
    incomplete_period_count: int
    target_hit_rate: float
    below_target_rate: float
    flat_rate: float
    negative_rate: float


@dataclass(frozen=True)
class ProfileComparisonResult:
    symbol: str
    analysis_period: str
    entries: list[ProfileComparisonEntry]
