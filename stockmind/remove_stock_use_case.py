from stockmind.infrastructure.watchlists.watchlist_repository import (
    WatchlistRepository
)

from stockmind.infrastructure.watchlists.watchlist_repository import (
    WatchlistRepository
)

from stockmind.application.watchlists.add_stock_use_case import (
    AddStockUseCase
)

from stockmind.application.watchlists.remove_stock_use_case import (
    RemoveStockUseCase
)


class RemoveStockUseCase:

    def execute(
        self,
        symbol: str
    ):

        WatchlistRepository().remove(
            symbol
        )

@app.get(
    "/watchlist-manage"
)
def watchlist_manage():
    return {
        "stocks": [
            {
            "symbol":
                item.symbol,

            "company_name":
                item.company_name
            }
            for item in (
                WatchlistRepository()
                .load_all()
            )
        ]
    }

@app.post(
    "/watchlist/{symbol}"
)
def add_stock(
    symbol: str
):

    added = (
        AddStockUseCase()
        .execute(
            symbol
        )
    )

    return {
        "symbol": symbol,
        "added": added
    }

@app.delete(
    "/watchlist/{symbol}"
)
def remove_stock(
    symbol: str
):

    RemoveStockUseCase().execute(
        symbol
    )

    return {
        "removed": symbol
    }