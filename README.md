import yfinance as yf

from stockmind.domain.history.indicator_chart_point import (
    IndicatorChartPoint
)

from stockmind.infrastructure.history.indicator_chart_data_repository import (
    IndicatorChartDataRepository
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

    if value != value:

        return None

    return float(
        value
    )


def calculate_rsi(
    data,
    window: int = 14
):

    delta = data["Close"].diff()

    gain = (
        delta.where(
            delta > 0,
            0
        )
        .rolling(
            window=window
        )
        .mean()
    )

    loss = (
        -delta.where(
            delta < 0,
            0
        )
        .rolling(
            window=window
        )
        .mean()
    )

    rs = gain / loss

    rsi = 100 - (
        100 / (1 + rs)
    )

    return rsi


def build_indicator_points(
    symbol: str
) -> list[IndicatorChartPoint]:

    ticker = yf.Ticker(
        symbol
    )

    data = ticker.history(
        period="1y"
    )

    data = data.copy()

    data["RSI_14"] = calculate_rsi(
        data
    )

    ema_12 = (
        data["Close"]
        .ewm(
            span=12
        )
        .mean()
    )

    ema_26 = (
        data["Close"]
        .ewm(
            span=26
        )
        .mean()
    )

    data["MACD"] = (
        ema_12
        - ema_26
    )

    data["MACD_Signal"] = (
        data["MACD"]
        .ewm(
            span=9
        )
        .mean()
    )

    data["MACD_Histogram"] = (
        data["MACD"]
        - data["MACD_Signal"]
    )

    points = []

    for index, row in data.iterrows():

        points.append(
            IndicatorChartPoint(
                symbol=symbol,

                trading_date=(
                    index.date()
                    .isoformat()
                ),

                rsi_14=_to_optional_float(
                    row["RSI_14"]
                ),

                macd=_to_optional_float(
                    row["MACD"]
                ),

                macd_signal=_to_optional_float(
                    row["MACD_Signal"]
                ),

                macd_histogram=_to_optional_float(
                    row["MACD_Histogram"]
                )
            )
        )

    return points


def main():

    repository = IndicatorChartDataRepository()

    for symbol in SYMBOLS:

        print(
            f"Refreshing indicator chart data for {symbol}"
        )

        points = build_indicator_points(
            symbol
        )

        repository.replace_for_symbol(
            symbol=symbol,
            points=points
        )

    print(
        "Indicator chart data refresh complete."
    )


if __name__ == "__main__":
    main()
