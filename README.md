from stockmind.application.use_cases.manage_watchlist_use_case import (
    ManageWatchlistUseCase
)


def main():

    use_case = (
        ManageWatchlistUseCase()
    )

    use_case.create(
        name="tech_stocks",
        symbols=[
            "NVDA",
            "AMD",
            "MSFT",
            "AAPL",
            "GOOGL"
        ]
    )

    watchlist = (
        use_case.load(
            "tech_stocks"
        )
    )

    print("\nWATCHLIST")

    print(
        f"Name: "
        f"{watchlist.name}"
    )

    for entry in watchlist.entries:

        print(
            entry.symbol
        )


if __name__ == "__main__":
    main()
