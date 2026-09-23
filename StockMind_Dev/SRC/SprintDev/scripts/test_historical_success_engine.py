import yfinance as yf

from stockmind.domain.historical_success.historical_success_engine import (
    HistoricalSuccessEngine,
)
from stockmind.infrastructure.profiles.profile_repository import ProfileRepository


def main():
    symbol = "NVDA"
    data = yf.Ticker(symbol).history(period="5y")
    engine = HistoricalSuccessEngine()

    for profile in ProfileRepository().get_all():
        result = engine.analyze(
            symbol=symbol,
            data=data,
            profile=profile,
            rule_set_name="mean_reversion",
            target_pct=0.08,
            lookahead_days=60,
            min_quality="MEDIUM",
        )
        print("\n==============================")
        print(f"PROFILE: {profile.name.upper()}")
        print("==============================")
        print(f"Setups:            {result.setup_count}")
        print(f"Complete:          {result.complete_count}")
        print(f"Target hit:        {result.target_hit_count}")
        print(f"Below target:      {result.below_target_count}")
        print(f"Flat:              {result.flat_count}")
        print(f"Negative:          {result.negative_count}")
        print(f"Incomplete:        {result.incomplete_count}")
        print(f"Target-hit rate:   {result.target_hit_rate:.2%}")
        print(f"Below-target rate: {result.below_target_rate:.2%}")
        print(f"Flat rate:         {result.flat_rate:.2%}")
        print(f"Negative rate:     {result.negative_rate:.2%}")
        print(f"Sample quality:    {result.sample_quality}")


if __name__ == "__main__":
    main()
