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
            rule_set_name="entry_setup",
            target_pct=0.08,
            lookahead_days=60,
            min_quality="MEDIUM",
            top_n_similar=50
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

        print(
            f"Average Similarity: "
            f"{result.average_similarity}"
        )


if __name__ == "__main__":
    main()
