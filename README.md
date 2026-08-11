from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class SimilarityCandidate:

    trading_date: date

    similarity_score: float

    successful: bool

    entry_price: float

    max_future_high: float
