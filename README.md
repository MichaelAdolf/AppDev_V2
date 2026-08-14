from random import randint, uniform

from stockmind.domain.history.historical_setup_entry import (
    HistoricalSetupEntry
)

from stockmind.infrastructure.history.historical_setup_repository import (
    HistoricalSetupRepository
)


def main():

    repo = (
        HistoricalSetupRepository()
    )

    for symbol in [
        "NVDA",
        "AMD",
        "MSFT"
    ]:

        for i in range(20):

            repo.save(
                HistoricalSetupEntry(
                    symbol=symbol,

                    setup_date=(
                        f"2025-{(i % 12)+1:02d}-01"
                    ),

                    entry_price=100 + i,

                    target_pct=0.08,

                    success=i % 3 != 0,

                    days_to_target=randint(
                        5,
                        60
                    ),

                    max_gain_pct=uniform(
                        5,
                        25
                    ),

                    max_drawdown_pct=uniform(
                        -15,
                        0
                    )
                )
            )


if __name__ == "__main__":
    main()
