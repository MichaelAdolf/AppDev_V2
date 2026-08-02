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

from stockmind.domain.scoring.scoring_engine import (
    ScoringEngine
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

    scoring_engine = ScoringEngine()

    score_result = (
        scoring_engine.calculate(
            strategy_results
        )
    )

    print("\n=== Score Result ===")
    print(score_result)


if __name__ == "__main__":
    main()
