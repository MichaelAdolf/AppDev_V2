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

from stockmind.domain.features.feature_engine import (
    FeatureEngine
)

ticker = yf.Ticker("NVDA")

df = ticker.history(
    period="1y"
)

indicator_engine = IndicatorEngine(
    indicators=[
        SMAIndicator(),
        EMAIndicator(),
        RSIIndicator(),
    ]
)

indicator_result = (
    indicator_engine.calculate(
        symbol="NVDA",
        data=df
    )
)

feature_engine = FeatureEngine()

features = feature_engine.build(
    indicator_result
)

print(features)
