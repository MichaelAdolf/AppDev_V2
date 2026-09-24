from dataclasses import dataclass

@dataclass(frozen=True)
class ChartPoint:

    symbol: str

    trading_date: str

    close_price: float

    bollinger_upper: float | None

    bollinger_middle: float | None

    bollinger_lower: float | None