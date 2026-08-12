from stockmind.domain.watchlists.watchlist import (
    Watchlist
)

from stockmind.domain.watchlists.watchlist_entry import (
    WatchlistEntry
)

from stockmind.infrastructure.watchlists.watchlist_repository import (
    WatchlistRepository
)


class ManageWatchlistUseCase:

    def create(
        self,
        name: str,
        symbols: list[str]
    ):

        watchlist = Watchlist(
            name=name,
            entries=[
                WatchlistEntry(
                    symbol=symbol
                )
                for symbol in symbols
            ]
        )

        WatchlistRepository().save(
            watchlist
        )

    def load(
        self,
        name: str
    ) -> Watchlist:

        return (
            WatchlistRepository()
            .load(
                name
            )
        )
