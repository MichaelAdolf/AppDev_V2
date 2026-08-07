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

from stockmind.infrastructure.profiles.profile_repository import (
    ProfileRepository
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

    print("\n=== INDICATOR RESULT ===")
    print(indicator_result)

    profile_repository = ProfileRepository()

    feature_engine = FeatureEngine()

    for profile in profile_repository.get_all():

        features = feature_engine.build(
            result=indicator_result,
            profile=profile
        )

        print(
            f"\n=== FEATURES FOR PROFILE: "
            f"{profile.name.upper()} ==="
        )

        print(features)


if __name__ == "__main__":
    main()
