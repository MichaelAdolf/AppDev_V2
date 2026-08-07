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

from stockmind.domain.indicators.macd_indicator import (
    MACDIndicator
)

from stockmind.domain.indicators.bollinger_indicator import (
    BollingerIndicator
)

from stockmind.domain.features.feature_engine import (
    FeatureEngine
)

from stockmind.domain.risk.risk_engine import (
    RiskEngine
)


def main():

    ticker = yf.Ticker("NVDA")

    df = ticker.history(
        period="1y"
    )

    indicator_engine = IndicatorEngine(
        indicators=[
            SMAIndicator(),
            EMAIndicator(),
            RSIIndicator(),
            MACDIndicator(),
            BollingerIndicator(),
        ]
    )

    indicator_result = indicator_engine.calculate(
        symbol="NVDA",
        data=df
    )

    features = FeatureEngine().build(
        indicator_result
    )

    risk_engine = RiskEngine()

    risk_result = risk_engine.calculate(
        features
    )

    print("\n=== RISK RESULT ===")
    print(risk_result)


if __name__ == "__main__":
    main()
