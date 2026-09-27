from stockmind.application.history.historical_opportunity_replay_use_case import HistoricalOpportunityReplayUseCase
from stockmind.infrastructure.watchlists.watchlist_repository import WatchlistRepository

PROFILES = ["conservative", "balanced", "aggressive"]


def main():
    symbols = WatchlistRepository().load_active_symbols()
    replay = HistoricalOpportunityReplayUseCase()
    for symbol in symbols:
        for profile in PROFILES:
            print(f"Historical opportunity replay: {symbol} | {profile}")
            entries = replay.execute(symbol=symbol, profile_name=profile, period="5y")
            print(f"  -> {len(entries)} daily opportunity entries")
    print("Historical opportunity replay complete.")


if __name__ == "__main__":
    main()
