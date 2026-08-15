from stockmind.application.use_cases.run_analysis_use_case import (
    RunAnalysisUseCase
)

from stockmind.infrastructure.watchlists.watchlist_repository import (
    WatchlistRepository
)


def get_symbols() -> list[str]:

    return (
        WatchlistRepository()
        .load_active_symbols()
    )


def main():

    profiles = [
        "conservative",
        "balanced",
        "aggressive"
    ]

    symbols = (
        get_symbols()
    )

    print(
        f"Found {len(symbols)} stocks in watchlist."
    )

    for profile_name in profiles:

        print(
            f"\nRefreshing profile: {profile_name}"
        )

        for symbol in symbols:

            print(
                f"Refreshing {symbol}"
            )

            RunAnalysisUseCase().execute(
                profile_name=profile_name,
                symbol=symbol
            )


if __name__ == "__main__":

    main()
