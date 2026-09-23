from dataclasses import dataclass

from stockmind.domain.history.historical_outcome import HistoricalOutcome


@dataclass(frozen=True)
class HistoricalSetupEntry:
    symbol: str
    profile_name: str
    analysis_period: str
    setup_date: str
    entry_price: float
    target_pct: float
    success: bool
    days_to_target: int | None
    max_gain_pct: float | None
    max_drawdown_pct: float | None
    window_start_date: str | None = None
    window_end_date: str | None = None
    window_end_return_pct: float | None = None
    outcome: str = HistoricalOutcome.INCOMPLETE_WINDOW.value
    is_complete: bool = False
