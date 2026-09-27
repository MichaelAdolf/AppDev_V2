from dataclasses import dataclass

@dataclass(frozen=True)
class IndicatorChartPoint:

    symbol: str

    trading_date: str

    rsi_14: float | None

    macd: float | None

    macd_signal: float | None

    macd_histogram: float | None

    adx: float | None

    plus_di: float | None

    minus_di: float | None

    stoch_k: float | None

    stoch_d: float | None
