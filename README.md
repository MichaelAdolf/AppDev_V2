import yfinance as yf

from stockmind.domain.historical_success.historical_success_engine import (
    HistoricalSuccessEngine
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

    engine = HistoricalSuccessEngine()

    profile_repository = ProfileRepository()

    for profile in profile_repository.get_all():

        result = engine.analyze(
            symbol=symbol,
            data=data,
            profile=profile,
            target_pct=0.08,
            lookahead_days=60
        )

        print(
            "\n=============================="
        )

        print(
            f"PROFILE: {profile.name.upper()}"
        )

        print(
            "=============================="
        )

        print(result)

        print(
            f"Success Rate: "
            f"{result.success_rate:.2%}"
        )


if __name__ == "__main__":
    main()
