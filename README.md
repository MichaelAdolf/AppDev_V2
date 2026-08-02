import yfinance as yf

from stockmind.domain.entities.market_data import (
    MarketDataPoint
)

from stockmind.infrastructure.market_data.market_data_provider import (
    MarketDataProvider
)


class YFinanceProvider(
    MarketDataProvider
):

    def fetch_history(
        self,
        symbol: str
    ) -> list:

        ticker = yf.Ticker(
            symbol
        )

        history = ticker.history(
            period="1y"
        )

        result = []

        for index, row in history.iterrows():

            result.append(
                MarketDataPoint(
                    symbol=symbol,
                    trading_date=index.date(),
                    open_price=float(
                        row["Open"]
                    ),
                    high_price=float(
                        row["High"]
                    ),
                    low_price=float(
                        row["Low"]
                    ),
                    close_price=float(
                        row["Close"]
                    ),
                    volume=int(
                        row["Volume"]
                    )
                )
            )

        return result
