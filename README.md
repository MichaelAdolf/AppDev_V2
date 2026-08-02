import yfinance as yf

from stockmind.domain.indicators.sma_indicator import (
    SMAIndicator
)

ticker = yf.Ticker(
    "NVDA"
)

df = ticker.history(
    period="1y"
)

indicator = SMAIndicator()

value = indicator.calculate(
    df
)

print(
    f"SMA20: {value}"
)
