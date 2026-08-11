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

from stockmind.domain.indicators.adx_indicator import (
    ADXIndicator
)

from stockmind.domain.indicators.stochastic_indicator import (
    StochasticIndicator
)

from stockmind.domain.features.feature_engine import (
    FeatureEngine
)

from stockmind.domain.rules.rule_engine import (
    RuleEngine
)

from stockmind.domain.core_setup.core_setup_engine import (
    CoreSetupEngine
)

from stockmind.domain.quality.quality_engine import (
    QualityEngine
)

from stockmind.infrastructure.rules.rule_set_repository import (
    RuleSetRepository
)

from stockmind.infrastructure.profiles.profile_repository import (
    ProfileRepository
)


def main():

    symbol = "NVDA"

    ticker = yf.Ticker(
        symbol
    )

    data = ticker.history(
        period="5y"
    )

    indicator_engine = IndicatorEngine(
        indicators=[
            SMAIndicator(),
            EMAIndicator(),
            RSIIndicator(),
            MACDIndicator(),
            BollingerIndicator(),
            ADXIndicator(),
            StochasticIndicator(),
        ]
    )

    indicator_result = indicator_engine.calculate(
        symbol=symbol,
        data=data
    )

    profile_repository = ProfileRepository()

    rule_set = (
        RuleSetRepository()
        .get_by_name(
            "entry_setup"
        )
    )

    core_setup_engine = CoreSetupEngine()

    quality_engine = QualityEngine()

    for profile in profile_repository.get_all():

        print(
            "\n=============================="
        )

        print(
            f"PROFILE: {profile.name.upper()}"
        )

        print(
            "=============================="
        )

        features = FeatureEngine().build(
            result=indicator_result,
            profile=profile
        )

        print("\nFeatures:")
        print(features)

        rule_engine = RuleEngine(
            rule_set=rule_set
        )

        rule_results = rule_engine.evaluate(
            features
        )

        print("\nRule Results:")
        for result in rule_results:
            print(result)

        core_setup_result = (
            core_setup_engine.evaluate(
                rule_results
            )
        )

        quality_result = (
            quality_engine.calculate(
                rule_results=rule_results,
                core_setup_result=core_setup_result
            )
        )

        print("\nCore Setup:")
        print(core_setup_result)

        print("\nQuality:")
        print(quality_result)


if __name__ == "__main__":
    main()
