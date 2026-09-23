from dataclasses import dataclass
from datetime import date

from stockmind.domain.history.historical_outcome import HistoricalOutcome


@dataclass(frozen=True)
class SimilarityCandidate:
    trading_date: date
    similarity_score: float
    successful: bool
    entry_price: float
    max_future_high: float
    outcome: str = HistoricalOutcome.INCOMPLETE_WINDOW.value
    is_complete: bool = False
    window_end_return_pct: float | None = None
    max_drawdown_pct: float | None = None
    days_to_target: int | None = None
