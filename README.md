from stockmind.infrastructure.history.fundamental_data_repository import (
    FundamentalDataRepository
)


def main():

    entry = (
        FundamentalDataRepository()
        .load(
            "NVDA"
        )
    )

    print(entry)


if __name__ == "__main__":
    main()
``
