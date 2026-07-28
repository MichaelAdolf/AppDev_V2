from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class MarketDataPoint:
    symbol: str

    trading_date: date

    open_price: float
    high_price: float
    low_price: float
    close_price: float

    volume: int
