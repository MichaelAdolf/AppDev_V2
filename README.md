from stockmind.infrastructure.history.historical_setup_repository import (
    HistoricalSetupRepository
)


def main():

    setups = (
        HistoricalSetupRepository()
        .load_by_symbol(
            symbol="NVDA",
            profile_name="balanced",
            analysis_period="1y"
        )
    )

    print(
        f"Found {len(setups)} setups"
    )

    for setup in setups[:10]:

        print(setup)


if __name__ == "__main__":

    main()
