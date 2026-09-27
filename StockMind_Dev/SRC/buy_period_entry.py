from dataclasses import dataclass


@dataclass(frozen=True)
class BuyPeriodEntry:
    symbol: str
    profile_name: str
    analysis_period: str
    start_date: str
    end_date: str
    calendar_duration_days: int
    buy_signal_count: int
    gap_days_total: int
    largest_gap_days: int
    entry_price: float
    target_pct: float
    outcome: str
    target_hit: bool
    days_to_target: int | None
    window_end_date: str | None
    window_end_return_pct: float | None
    max_gain_pct: float | None
    max_drawdown_pct: float | None
    is_complete: bool
