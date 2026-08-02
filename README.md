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

from stockmind.domain.rules.rule_set import (
    RuleSet
)

from stockmind.domain.rules.rsi_oversold_rule import (
    RSIOversoldRule
)

from stockmind.domain.rules.macd_positive_rule import (
    MACDPositiveRule
)

from stockmind.domain.rules.lower_bollinger_rule import (
    LowerBollingerRule
)

from stockmind.domain.rules.trend_rule import (
    TrendRule
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

    # -------------------------------------------------
    # Marktdaten laden
    # -------------------------------------------------

    ticker = yf.Ticker("NVDA")

    df = ticker.history(
        period="1y"
    )

    # -------------------------------------------------
    # Indicator Engine
    # -------------------------------------------------

    indicator_engine = IndicatorEngine(
        indicators=[
            SMAIndicator(),
            EMAIndicator(),
            RSIIndicator(),
            MACDIndicator(),
            BollingerIndicator(),
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

    # -------------------------------------------------
    # Feature Engine
    # -------------------------------------------------

    feature_engine = FeatureEngine()

    features = feature_engine.build(
        indicator_result
    )

    print("\n=== Feature Snapshot ===")
    print(features)

    # -------------------------------------------------
    # Mean Reversion Rule Set
    # -------------------------------------------------

    mean_reversion_rules = RuleSet(
        name="mean_reversion",

        rules=[
            RSIOversoldRule(),
            LowerBollingerRule(),
        ]
    )

    mean_reversion_engine = RuleEngine(
        rule_set=mean_reversion_rules
    )

    mean_reversion_results = (
        mean_reversion_engine.evaluate(
            features
        )
    )

    print_rule_results(
        "MEAN REVERSION RULES",
        mean_reversion_results
    )

    # -------------------------------------------------
    # Trend Following Rule Set
    # -------------------------------------------------

    trend_following_rules = RuleSet(
        name="trend_following",

        rules=[
            TrendRule(),
            MACDPositiveRule(),
        ]
    )

    trend_following_engine = RuleEngine(
        rule_set=trend_following_rules
    )

    trend_following_results = (
        trend_following_engine.evaluate(
            features
        )
    )

    print_rule_results(
        "TREND FOLLOWING RULES",
        trend_following_results
    )


if __name__ == "__main__":
    main()
