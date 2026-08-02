import yfinance as yf

from stockmind.domain.indicators.indicator_engine import (
    IndicatorEngine
)

from stockmind.domain.indicators.sma_indicator import (
    SMAIndicator
)

ticker = yf.Ticker(
    "NVDA"
)

df = ticker.history(
    period="1y"
)

engine = IndicatorEngine(
    indicators=[
        SMAIndicator()
    ]
)

result = engine.calculate(
    symbol="NVDA",
    data=df
)

print(result)
