from collections import Counter

from stockmind.application.history.historical_setup_replay_use_case import (
    HistoricalSetupReplayUseCase,
)
from stockmind.infrastructure.watchlists.watchlist_repository import (
    WatchlistRepository,
)


PROFILES = [
    "conservative",
    "balanced",
    "aggressive",
]

PERIODS = [
    "1m",
    "6m",
    "1y",
    "3y",
    "5y",
]


def main():
    symbols = WatchlistRepository().load_active_symbols()
    print(f"Found {len(symbols)} symbols in watchlist.")
    use_case = HistoricalSetupReplayUseCase()

    for symbol in symbols:
        for profile in PROFILES:
            for period in PERIODS:
                print(
                    "Replaying setups: "
                    f"{symbol} | {profile} | {period}"
                )
                entries = use_case.execute(
                    symbol=symbol,
                    profile_name=profile,
                    analysis_period=period,
                    target_pct=0.08,
                    lookahead_days=60,
                )
                outcomes = Counter(entry.outcome for entry in entries)
                print(f"  -> {len(entries)} setups")
                print(
                    "  -> TARGET_HIT={target}, "
                    "BELOW_TARGET={below}, "
                    "FLAT={flat}, "
                    "NEGATIVE={negative}, "
                    "INCOMPLETE_WINDOW={incomplete}".format(
                        target=outcomes.get("TARGET_HIT", 0),
                        below=outcomes.get("BELOW_TARGET", 0),
                        flat=outcomes.get("FLAT", 0),
                        negative=outcomes.get("NEGATIVE", 0),
                        incomplete=outcomes.get("INCOMPLETE_WINDOW", 0),
                    )
                )


if __name__ == "__main__":
    main()
