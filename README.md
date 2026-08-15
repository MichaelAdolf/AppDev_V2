from stockmind.application.history.historical_setup_replay_use_case import (
    HistoricalSetupReplayUseCase
)

from stockmind.infrastructure.watchlists.watchlist_repository import (
    WatchlistRepository
)


PROFILES = [
    "conservative",
    "balanced",
    "aggressive"
]


PERIODS = [
    "1m",
    "6m",
    "1y",
    "3y",
    "5y"
]


def main():

    symbols = (
        WatchlistRepository()
        .load_active_symbols()
    )

    print(
        f"Found {len(symbols)} symbols in watchlist."
    )

    use_case = (
        HistoricalSetupReplayUseCase()
    )

    for symbol in symbols:

        for profile in PROFILES:

            for period in PERIODS:

                print(
                    f"Replaying setups: "
                    f"{symbol} | {profile} | {period}"
                )

                entries = (
                    use_case.execute(
                        symbol=symbol,
                        profile_name=profile,
                        analysis_period=period,
                        target_pct=0.08,
                        lookahead_days=60
                    )
                )

                print(
                    f"  -> {len(entries)} setups"
                )


if __name__ == "__main__":

    main()
