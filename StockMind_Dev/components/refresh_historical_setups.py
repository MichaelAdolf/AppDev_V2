from collections import Counter

from stockmind.application.history.historical_setup_replay_use_case import HistoricalSetupReplayUseCase
from stockmind.application.history.refresh_buy_periods_use_case import RefreshBuyPeriodsUseCase
from stockmind.infrastructure.watchlists.watchlist_repository import WatchlistRepository

PROFILES = ["conservative", "balanced", "aggressive"]
PERIODS = ["1m", "6m", "1y", "3y", "5y"]


def main():
    symbols = WatchlistRepository().load_active_symbols()
    print(f"Found {len(symbols)} symbols in watchlist.")
    replay = HistoricalSetupReplayUseCase()
    period_refresh = RefreshBuyPeriodsUseCase()

    for symbol in symbols:
        for profile in PROFILES:
            for analysis_period in PERIODS:
                print(f"Replaying: {symbol} | {profile} | {analysis_period}")
                entries = replay.execute(
                    symbol=symbol,
                    profile_name=profile,
                    analysis_period=analysis_period,
                    target_pct=0.08,
                    lookahead_days=60,
                )
                periods = period_refresh.execute(
                    symbol=symbol,
                    profile_name=profile,
                    analysis_period=analysis_period,
                    max_gap_days=3,
                    target_pct=0.08,
                )
                outcomes = Counter(period.outcome for period in periods)
                print(
                    f"  -> {len(entries)} BUY days, {len(periods)} BUY periods | "
                    f"TARGET_HIT={outcomes.get('TARGET_HIT', 0)}, "
                    f"BELOW_TARGET={outcomes.get('BELOW_TARGET', 0)}, "
                    f"FLAT={outcomes.get('FLAT', 0)}, "
                    f"NEGATIVE={outcomes.get('NEGATIVE', 0)}, "
                    f"INCOMPLETE={outcomes.get('INCOMPLETE_WINDOW', 0)}"
                )


if __name__ == "__main__":
    main()
