import yfinance as yf

from stockmind.domain.history.fundamental_data_entry import (
    FundamentalDataEntry
)

from stockmind.infrastructure.history.fundamental_data_repository import (
    FundamentalDataRepository
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


def _to_optional_float(
    value
):

    if value is None:

        return None

    try:

        return float(
            value
        )

    except Exception:

        return None


def _to_optional_text(
    value
):

    if value is None:

        return None

    return str(
        value
    )


def build_entry(
    symbol: str
) -> FundamentalDataEntry:

    ticker = yf.Ticker(
        symbol
    )

    info = ticker.info

    return FundamentalDataEntry(
        symbol=symbol,

        company_name=_to_optional_text(
            info.get(
                "longName"
            )
        ),

        sector=_to_optional_text(
            info.get(
                "sector"
            )
        ),

        industry=_to_optional_text(
            info.get(
                "industry"
            )
        ),

        market_cap=_to_optional_float(
            info.get(
                "marketCap"
            )
        ),

        trailing_pe=_to_optional_float(
            info.get(
                "trailingPE"
            )
        ),

        forward_pe=_to_optional_float(
            info.get(
                "forwardPE"
            )
        ),

        profit_margins=_to_optional_float(
            info.get(
                "profitMargins"
            )
        ),

        revenue_growth=_to_optional_float(
            info.get(
                "revenueGrowth"
            )
        ),

        recommendation_key=_to_optional_text(
            info.get(
                "recommendationKey"
            )
        ),

        target_mean_price=_to_optional_float(
            info.get(
                "targetMeanPrice"
            )
        )
    )


def main():

    repository = FundamentalDataRepository()

    count = 0

    for symbol in SYMBOLS:

        print(
            f"Refreshing fundamentals for {symbol}"
        )

        entry = build_entry(
            symbol
        )

        repository.save(
            entry
        )

        count += 1

    print(
        f"Refreshed fundamentals for {count} symbols."
    )


if __name__ == "__main__":
    main()
