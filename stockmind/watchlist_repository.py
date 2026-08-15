import sqlite3

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
            CREATE TABLE IF NOT EXISTS watchlist (

                symbol TEXT PRIMARY KEY,

                company_name TEXT NOT NULL,

                active INTEGER NOT NULL,

                created_at TEXT NOT NULL
            )
            """
        )

        connection.commit()

        connection.close()

    def load_all(
        self
    ) -> list[WatchlistEntry]:

        connection = sqlite3.connect(
            self._database_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT

                symbol,
                company_name,
                active,
                created_at

            FROM watchlist

            ORDER BY symbol
            """
        )

        rows = cursor.fetchall()

        connection.close()

        return [
            WatchlistEntry(
                symbol=row[0],
                company_name=row[1],
                active=bool(
                    row[2]
                ),
                created_at=row[3]
            )
            for row in rows
        ]

    def exists(
        self,
        symbol: str
    ) -> bool:

        connection = sqlite3.connect(
            self._database_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)

            FROM watchlist

            WHERE symbol = ?
            """,
            (
                symbol.upper(),
            )
        )

        count = cursor.fetchone()[0]

        connection.close()

        return count > 0

    def add(
        self,
        entry: WatchlistEntry
    ):

        if self.exists(
            entry.symbol
        ):

            return

        connection = sqlite3.connect(
            self._database_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO watchlist
            (
                symbol,
                company_name,
                active,
                created_at
            )
            VALUES
            (
                ?, ?, ?, ?
            )
            """,
            (
                entry.symbol,
                entry.company_name,
                int(
                    entry.active
                ),
                entry.created_at
            )
        )

        connection.commit()

        connection.close()

    def remove(
        self,
        symbol: str
    ):

        connection = sqlite3.connect(
            self._database_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM watchlist

            WHERE symbol = ?
            """,
            (
                symbol.upper(),
            )
        )

        connection.commit()

        connection.close()