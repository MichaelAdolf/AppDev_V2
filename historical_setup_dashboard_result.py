from dataclasses import dataclass

from stockmind.domain.history.historical_setup_entry import HistoricalSetupEntry

@dataclass(frozen=True)
class HistoricalSetupDashboardResult:
    setup_count: int

    successful_count: int

    failed_count: int

    success_rate: float

    average_days: float

    average_gain: float

    average_drawdown: float

    setups: list[HistoricalSetupEntry]