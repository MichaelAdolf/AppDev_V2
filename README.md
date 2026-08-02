from datetime import date

from stockmind.domain.entities.market_data import (
    MarketDataPoint
)

from stockmind.infrastructure.market_data.market_data_provider import (
    MarketDataProvider
)


class MockProvider(
    MarketDataProvider
):

    def fetch_history(
        self,
        symbol: str
    ):

        return [
            MarketDataPoint(
                symbol=symbol,
                trading_date=date.today(),
                open_price=100,
                high_price=105,
                low_price=95,
                close_price=102,
                volume=1000000
            )
        ]
