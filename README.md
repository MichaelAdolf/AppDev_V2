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

from stockmind.infrastructure.profiles.profile_repository import (
    ProfileRepository
)

from stockmind.infrastructure.rules.rule_set_repository import (
    RuleSetRepository
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

    rule_set = rule_set_repository.get_by_name(
        "entry_setup"
    )

    core_setup_engine = CoreSetupEngine()

    quality_engine = QualityEngine()

    confidence_engine = ConfidenceEngine()

    risk_engine = RiskEngine()

    signal_engine = SignalEngine()

    historical_success_engine = HistoricalSuccessEngine()

    for profile in profile_repository.get_all():

        print(
            "\n\n=========================================="
        )

        print(
            f"PROFILE: {profile.name.upper()}"
        )

        print(
            "=========================================="
        )

        features = feature_engine.build(
            result=indicator_result,
            profile=profile
        )

        rule_engine = RuleEngine(
            rule_set=rule_set
        )

        rule_results = rule_engine.evaluate(
            features
        )

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

        #
        # Historische Analyse
        # ALLE Setups
        #

        historical_all = (
            historical_success_engine.analyze(
                symbol=symbol,
                data=data,
                profile=profile,
                rule_set_name="entry_setup",
                target_pct=0.08,
                lookahead_days=60,
                min_quality="MEDIUM",
                top_n_similar=None
            )
        )

        #
        # Historische Analyse
        # ÄHNLICHSTE Setups
        #

        historical_similar = (
            historical_success_engine.analyze(
                symbol=symbol,
                data=data,
                profile=profile,
                rule_set_name="entry_setup",
                target_pct=0.08,
                lookahead_days=60,
                min_quality="MEDIUM",
                top_n_similar=50
            )
        )

        #
        # Confidence nur Rules
        #

        confidence_rule = (
            confidence_engine.calculate(
                rule_results=rule_results,
                historical_success_result=None
            )
        )

        #
        # Confidence mit allen Setups
        #

        confidence_all = (
            confidence_engine.calculate(
                rule_results=rule_results,
                historical_success_result=historical_all
            )
        )

        #
        # Confidence mit Similarity
        #

        confidence_similar = (
            confidence_engine.calculate(
                rule_results=rule_results,
                historical_success_result=historical_similar
            )
        )

        risk_result = (
            risk_engine.calculate(
                features
            )
        )

        signal_result = (
            signal_engine.create_signal(
                symbol=symbol,
                quality_result=quality_result,
                confidence_result=confidence_similar,
                risk_result=risk_result
            )
        )

        print("\nCore Setup:")
        print(core_setup_result)

        print("\nQuality:")
        print(quality_result)

        print("\n--- HISTORICAL ALL SETUPS ---")
        print(historical_all)

        print(
            f"Success Rate: "
            f"{historical_all.success_rate:.2%}"
        )

        print("\n--- HISTORICAL SIMILAR SETUPS ---")
        print(historical_similar)

        print(
            f"Success Rate: "
            f"{historical_similar.success_rate:.2%}"
        )

        print(
            f"Average Similarity: "
            f"{historical_similar.average_similarity}"
        )

        print("\n--- RULE CONFIDENCE ---")
        print(confidence_rule)

        print("\n--- ALL SETUPS CONFIDENCE ---")
        print(confidence_all)

        print("\n--- SIMILARITY CONFIDENCE ---")
        print(confidence_similar)

        print("\nRisk:")
        print(risk_result)

        print("\nFinal Signal:")
        print(signal_result)


if __name__ == "__main__":
    main()
