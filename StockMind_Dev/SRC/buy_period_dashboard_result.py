from dataclasses import dataclass
from stockmind.domain.history.buy_period_entry import BuyPeriodEntry


@dataclass(frozen=True)
class TargetTimeBucket:
    label: str
    count: int
    rate: float


@dataclass(frozen=True)
class BuyPeriodStatistics:
    complete_period_count: int
    incomplete_period_count: int
    target_hit_count: int
    below_target_count: int
    flat_count: int
    negative_count: int
    target_hit_rate: float
    below_target_rate: float
    flat_rate: float
    negative_rate: float
    average_days_to_target: float
    median_days_to_target: float
    fastest_days_to_target: int | None
    slowest_days_to_target: int | None
    target_time_buckets: list[TargetTimeBucket]
    average_calendar_duration_days: float
    median_calendar_duration_days: float
    duration_q25_days: float
    duration_q75_days: float
    average_buy_signal_count: float
    average_max_gain_pct: float
    average_max_drawdown_pct: float
    median_max_drawdown_pct: float
    successful_average_max_gain_pct: float
    successful_average_max_drawdown_pct: float
    failed_average_max_gain_pct: float
    failed_average_max_drawdown_pct: float
    sample_quality: str


@dataclass(frozen=True)
class BuyPeriodDashboardResult:
    symbol: str
    profile_name: str
    analysis_period: str
    max_gap_days: int
    period_count: int
    statistics: BuyPeriodStatistics
    active_period: BuyPeriodEntry | None
    active_period_phase: str
    periods: list[BuyPeriodEntry]
