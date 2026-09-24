from dataclasses import dataclass

from stockmind.domain.history.buy_period_entry import BuyPeriodEntry


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
    average_calendar_duration_days: float
    average_buy_signal_count: float
    average_max_gain_pct: float
    average_max_drawdown_pct: float


@dataclass(frozen=True)
class BuyPeriodDashboardResult:
    symbol: str
    profile_name: str
    analysis_period: str
    max_gap_days: int
    period_count: int
    statistics: BuyPeriodStatistics
    active_period: BuyPeriodEntry | None
    periods: list[BuyPeriodEntry]
