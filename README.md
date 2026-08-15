from stockmind.infrastructure.watchlist.watchlist_repository import (
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
