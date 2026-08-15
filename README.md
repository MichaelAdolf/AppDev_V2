from stockmind.infrastructure.watchlists.watchlist_repository import (
    WatchlistRepository
)


class RemoveStockUseCase:

    def execute(
        self,
        symbol: str
    ):

        WatchlistRepository().remove(
            symbol
        )
