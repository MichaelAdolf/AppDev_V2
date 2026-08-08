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

from stockmind.domain.historical_success.historical_success_engine import (
    HistoricalSuccessEngine
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

    feature_engine = FeatureEngine()

    profile_repository = ProfileRepository()

    rule_set_repository = RuleSetRepository()

    quality_engine = QualityEngine()

    confidence_engine = ConfidenceEngine()

    risk_engine = RiskEngine()

    signal_engine = SignalEngine()

    historical_success_engine = HistoricalSuccessEngine()

    for profile in profile_repository.get_all():

        print(
            "\n\n=============================="
        )

        print(
            f"PROFILE: {profile.name.upper()}"
        )

        print(
            "=============================="
        )

        features = feature_engine.build(
            result=indicator_result,
            profile=profile
        )

        print("\nFeatures:")
        print(features)

        for rule_set in rule_set_repository.get_all():

            print(
                f"\n--- RULE SET: "
                f"{rule_set.name.upper()} ---"
            )

            rule_engine = RuleEngine(
                rule_set=rule_set
            )

            rule_results = rule_engine.evaluate(
                features
            )

            quality_result = quality_engine.calculate(
                rule_results
            )

            historical_result = (
                historical_success_engine.analyze(
                    symbol=symbol,
                    data=data,
                    profile=profile,
                    rule_set_name=rule_set.name,
                    target_pct=0.08,
                    lookahead_days=60,
                    min_quality="MEDIUM"
                )
            )

            confidence_result = (
                confidence_engine.calculate(
                    rule_results=rule_results,
                    historical_success_result=historical_result
                )
            )

            risk_result = risk_engine.calculate(
                features
            )

            signal = signal_engine.create_signal(
                symbol=symbol,
                quality_result=quality_result,
                confidence_result=confidence_result,
                risk_result=risk_result
            )

            print("\nRule Results:")
            for result in rule_results:
                print(result)

            print("\nQuality:")
            print(quality_result)

            print("\nHistorical Success:")
            print(historical_result)

            print("\nConfidence:")
            print(confidence_result)

            print("\nRisk:")
            print(risk_result)

            print("\nSignal:")
            print(signal)


if __name__ == "__main__":
    main()
