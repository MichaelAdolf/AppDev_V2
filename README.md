import yfinance as yf

from stockmind.domain.indicators.adx_indicator import (
    ADXIndicator
)


def main():

    ticker = yf.Ticker("NVDA")

    df = ticker.history(
        period="1y"
    )

    indicator = ADXIndicator()

    value = indicator.calculate(
        df
    )

    print(
        f"ADX14: {value}"
    )


if __name__ == "__main__":
    main()
