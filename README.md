import yfinance as yf

from stockmind.domain.indicators.indicator_engine import (
    IndicatorEngine
)

from stockmind.domain.indicators.sma_indicator import (
    SMAIndicator
)

from stockmind.domain.indicators.ema_indicator import (
    EMAIndicator
)

from stockmind.domain.indicators.rsi_indicator import (
    RSIIndicator
)

ticker = yf.Ticker(
    "NVDA"
)

df = ticker.history(
    period="1y"
)

engine = IndicatorEngine(
    indicators=[
        SMAIndicator(),
        EMAIndicator(),
        RSIIndicator(),
    ]
)

result = engine.calculate(
    symbol="NVDA",
    data=df
)

print(result)
