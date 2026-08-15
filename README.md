from datetime import date
from datetime import timedelta
from random import randint
from random import uniform

from stockmind.domain.history.historical_setup_entry import (
    HistoricalSetupEntry
)

from stockmind.infrastructure.history.historical_setup_repository import (
    HistoricalSetupRepository
)


SYMBOLS = [
    "NVDA",
    "AMD",
    "MSFT",
    "AAPL",
    "GOOGL",
    "AMZN",
    "META",
    "PLTR",
    "TSLA",
]


def main():

    repo = HistoricalSetupRepository()

    count = 0

    today = date.today()

    for symbol in SYMBOLS:

        repo.delete_by_symbol(
            symbol
        )

        for i in range(18):

            setup_date = (
                today
                - timedelta(
                    days=30 * (i + 1)
                )
            )

            success = (
                i % 3 != 0
            )

            days_to_target = (
                randint(
                    5,
                    60
                )
                if success
                else 60
            )

            repo.save(
                HistoricalSetupEntry(
                    symbol=symbol,

                    setup_date=(
                        setup_date.isoformat()
                    ),

                    entry_price=(
                        100
                        + uniform(
                            -15.0,
                            35.0
                        )
                    ),

                    target_pct=0.08,

                    success=success,

                    days_to_target=days_to_target,

                    max_gain_pct=uniform(
                        8.0,
                        25.0
                    )
                    if success
                    else uniform(
                        0.0,
                        7.5
                    ),

                    max_drawdown_pct=uniform(
                        -15.0,
                        -1.0
                    )
                )
            )

            count += 1

    print(
        f"Created {count} historical setups."
    )


if __name__ == "__main__":
    main()
