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

from stockmind.domain.features.feature_engine import (
    FeatureEngine
)

from stockmind.domain.rules.rule_engine import (
    RuleEngine
)

from stockmind.infrastructure.rules.rule_set_repository import (
    RuleSetRepository
)

from stockmind.infrastructure.profiles.profile_repository import (
    ProfileRepository
)

from stockmind.domain.quality.quality_engine import (
    QualityEngine
)

from stockmind.domain.confidence.confidence_engine import (
    ConfidenceEngine
)

from stockmind.domain.risk.risk_engine import (
    RiskEngine
)

from stockmind.domain.signals.signal_engine import (
    SignalEngine
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
            ADXIndicator(),
        ]
    )

    indicator_result = indicator_engine.calculate(
        symbol="NVDA",
        data=df
    )

    feature_engine = FeatureEngine()

    profile_repository = ProfileRepository()

    rule_set_repository = RuleSetRepository()

    quality_engine = QualityEngine()

    confidence_engine = ConfidenceEngine()

    risk_engine = RiskEngine()

    signal_engine = SignalEngine()

    for profile in profile_repository.get_all():

        print(
            f"\n\n=============================="
        )

        print(
            f"PROFILE: {profile.name.upper()}"
        )

        print(
            f"=============================="
        )

        features = feature_engine.build(
            result=indicator_result,
            profile=profile
        )

        print("\nFeatures:")
        print(features)

        for rule_set in (
            rule_set_repository.get_all()
        ):

            print(
                f"\n--- RULE SET: "
                f"{rule_set.name.upper()} ---"
            )

            rule_engine = RuleEngine(
                rule_set=rule_set
            )

            rule_results = (
                rule_engine.evaluate(
                    features
                )
            )

            quality_result = (
                quality_engine.calculate(
                    rule_results
                )
            )

            confidence_result = (
                confidence_engine.calculate(
                    rule_results
                )
            )

            risk_result = (
                risk_engine.calculate(
                    features
                )
            )

            signal = (
                signal_engine.create_signal(
                    symbol="NVDA",
                    quality_result=quality_result,
                    confidence_result=confidence_result,
                    risk_result=risk_result
                )
            )

            print("\nRule Results:")
            for result in rule_results:
                print(result)

            print("\nQuality:")
            print(quality_result)

            print("\nConfidence:")
            print(confidence_result)

            print("\nRisk:")
            print(risk_result)

            print("\nSignal:")
            print(signal)


if __name__ == "__main__":
    main()
