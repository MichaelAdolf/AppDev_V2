from datetime import datetime

import yfinance as yf

from stockmind.domain.watchlists.watchlist_entry import (
    WatchlistEntry
)

from stockmind.infrastructure.watchlists.watchlist_repository import (
    WatchlistRepository
)


class AddStockUseCase:

    def execute(
        self,
        symbol: str
    ):

        symbol = (
            symbol.upper()
            .strip()
        )

        repository = (
            WatchlistRepository()
        )

        if repository.exists(
            symbol
        ):

            return False

        info = (
            yf.Ticker(
                symbol
            ).info
        )

        company_name = (
            info.get(
                "longName"
            )
            or symbol
        )

        repository.add(
            WatchlistEntry(
                symbol=symbol,
                company_name=company_name,
                active=True,
                created_at=(
                    datetime.utcnow()
                    .isoformat()
                )
            )
        )

        return True