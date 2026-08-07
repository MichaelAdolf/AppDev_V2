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

from stockmind.domain.rules.rule_engine import (
    RuleEngine
)

from stockmind.domain.quality.quality_engine import (
    QualityEngine
)

from stockmind.infrastructure.rules.rule_set_repository import (
    RuleSetRepository
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

    rule_set_repository = RuleSetRepository()

    quality_engine = QualityEngine()

    for rule_set in rule_set_repository.get_all():

        print(
            f"\n=== {rule_set.name.upper()} ==="
        )

        rule_engine = RuleEngine(
            rule_set=rule_set
        )

        rule_results = rule_engine.evaluate(
            features
        )

        quality_result = (
            quality_engine.calculate(
                rule_results
            )
        )

        print(
            quality_result
        )


if __name__ == "__main__":
    main()
