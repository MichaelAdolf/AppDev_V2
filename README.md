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

from stockmind.infrastructure.rules.rule_set_repository import (
    RuleSetRepository
)


def print_rule_results(
    title: str,
    results
):

    print(f"\n=== {title} ===")

    total_score = 0

    for result in results:

        print(result)

        total_score += result.score

    print(
        f"\nTotal Rule Score: {total_score}"
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

    print("\n=== Indicator Result ===")
    print(indicator_result)

    feature_engine = FeatureEngine()

    features = feature_engine.build(
        indicator_result
    )

    print("\n=== Feature Snapshot ===")
    print(features)

    rule_set_repository = RuleSetRepository()

    for rule_set in rule_set_repository.get_all():

        rule_engine = RuleEngine(
            rule_set=rule_set
        )

        rule_results = rule_engine.evaluate(
            features
        )

        print_rule_results(
            rule_set.name.upper(),
            rule_results
        )


if __name__ == "__main__":
    main()
