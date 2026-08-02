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

from stockmind.domain.strategies.strategy_engine import (
    StrategyEngine
)

from stockmind.domain.strategies.mean_reversion_strategy import (
    MeanReversionStrategy
)


def main():

    # Historische Marktdaten laden
    ticker = yf.Ticker("NVDA")

    df = ticker.history(
        period="1y"
    )

    # Indicator Engine
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

    print("\n=== Indicator Result ===")
    print(indicator_result)

    # Feature Engine
    feature_engine = FeatureEngine()

    features = feature_engine.build(
        indicator_result
    )

    print("\n=== Feature Snapshot ===")
    print(features)

    # Strategy Engine
    strategy_engine = StrategyEngine(
        strategies=[
            MeanReversionStrategy()
        ]
    )

    strategy_results = (
        strategy_engine.evaluate(
            features
        )
    )

    print("\n=== Strategy Results ===")

    for result in strategy_results:
        print(result)


if __name__ == "__main__":
    main()
