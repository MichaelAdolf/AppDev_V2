from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class MarketFeatureSnapshot:
    symbol: str
    rsi: float
    sma_20: float
    ema_20: float
    macd: float
    bollinger_position: float
    is_oversold: bool
    is_overbought: bool
    ema_above_sma: bool
    macd_positive: bool
    near_lower_bollinger: bool
    adx_14: float | None = None
    adx_trend_strength: bool = False
    stoch_k_14: float | None = None
    stoch_oversold: bool = False
