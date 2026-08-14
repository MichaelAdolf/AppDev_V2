import yfinance as yf

from stockmind.domain.history.chart_point import (
    ChartPoint
)

from stockmind.infrastructure.history.chart_data_repository import (
    ChartDataRepository
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


def build_chart_points(
    symbol: str
) -> list[ChartPoint]:

    ticker = yf.Ticker(
        symbol
    )

    data = ticker.history(
        period="1y"
    )

    data = data.copy()

    data["BB_Middle"] = (
        data["Close"]
        .rolling(
            window=20
        )
        .mean()
    )

    data["BB_Std"] = (
        data["Close"]
        .rolling(
            window=20
        )
        .std()
    )

    data["BB_Upper"] = (
        data["BB_Middle"]
        + data["BB_Std"] * 2
    )

    data["BB_Lower"] = (
        data["BB_Middle"]
        - data["BB_Std"] * 2
    )

    points = []

    for index, row in data.iterrows():

        points.append(
            ChartPoint(
                symbol=symbol,

                trading_date=(
                    index.date()
                    .isoformat()
                ),

                close_price=float(
                    row["Close"]
                ),

                bollinger_upper=(
                    None
                    if row["BB_Upper"] != row["BB_Upper"]
                    else float(row["BB_Upper"])
                ),

                bollinger_middle=(
                    None
                    if row["BB_Middle"] != row["BB_Middle"]
                    else float(row["BB_Middle"])
                ),

                bollinger_lower=(
                    None
                    if row["BB_Lower"] != row["BB_Lower"]
                    else float(row["BB_Lower"])
                )
            )
        )

    return points


def main():

    repository = ChartDataRepository()

    for symbol in SYMBOLS:

        print(
            f"Refreshing chart data for {symbol}"
        )

        points = build_chart_points(
            symbol
        )

        repository.replace_for_symbol(
            symbol=symbol,
            points=points
        )

    print(
        "Chart data refresh complete."
    )


if __name__ == "__main__":
    main()
