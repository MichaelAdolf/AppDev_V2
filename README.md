import sqlite3

from stockmind.domain.watchlists.watchlist import (
    Watchlist
)

from stockmind.domain.watchlists.watchlist_entry import (
    WatchlistEntry
)


class WatchlistRepository:

    def __init__(
        self,
        database_path: str = "stockmind.db"
    ):

        self._database_path = database_path

        self._initialize()

    def _initialize(
        self
    ):

        connection = sqlite3.connect(
            self._database_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS watchlists (

                name TEXT NOT NULL,

                symbol TEXT NOT NULL
            )
            """
        )

        connection.commit()

        connection.close()

    def save(
        self,
        watchlist: Watchlist
    ):

        connection = sqlite3.connect(
            self._database_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM watchlists
            WHERE name = ?
            """,
            (watchlist.name,)
        )

        for entry in watchlist.entries:

            cursor.execute(
                """
                INSERT INTO watchlists
                (
                    name,
                    symbol
                )
                VALUES
                (
                    ?,
                    ?
                )
                """,
                (
                    watchlist.name,
                    entry.symbol
                )
            )

        connection.commit()

        connection.close()

    def load(
        self,
        name: str
    ) -> Watchlist:

        connection = sqlite3.connect(
            self._database_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT symbol
            FROM watchlists
            WHERE name = ?
            """,
            (name,)
        )

        rows = cursor.fetchall()

        connection.close()

        entries = [
            WatchlistEntry(
                symbol=row[0]
            )
            for row in rows
        ]

        return Watchlist(
            name=name,
            entries=entries
        )
