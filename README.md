from dataclasses import dataclass


@dataclass(frozen=True)
class BuyPeriodEntry:

    start_date: str

    end_date: str

    setup_count: int

    successful_count: int

    failed_count: int

    success_rate: float

    average_days_to_target: float

    max_gain_pct: float

    max_drawdown_pct: float

    status: str


@dataclass(frozen=True)
class BuyPeriodDashboardResult:

    symbol: str

    period_count: int

    successful_period_count: int

    failed_period_count: int

    mixed_period_count: int

    overall_success_rate: float

    average_days_to_target: float

    average_max_gain_pct: float

    average_max_drawdown_pct: float

    periods: list[BuyPeriodEntry]
