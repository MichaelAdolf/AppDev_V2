import sqlite3

from stockmind.domain.history.historical_setup_entry import (
    HistoricalSetupEntry
)


class HistoricalSetupRepository:

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
            CREATE TABLE IF NOT EXISTS historical_setups (

                symbol TEXT NOT NULL,

                profile_name TEXT NOT NULL,

                analysis_period TEXT NOT NULL,

                setup_date TEXT NOT NULL,

                entry_price REAL,

                target_pct REAL,

                success INTEGER,

                days_to_target INTEGER,

                max_gain_pct REAL,

                max_drawdown_pct REAL
            )
            """
        )

        connection.commit()

        connection.close()

    def save(
        self,
        entry: HistoricalSetupEntry
    ):

        connection = sqlite3.connect(
            self._database_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO historical_setups
            (
                symbol,
                profile_name,
                analysis_period,
                setup_date,
                entry_price,
                target_pct,
                success,
                days_to_target,
                max_gain_pct,
                max_drawdown_pct
            )
            VALUES
            (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
            """,
            (
                entry.symbol,
                entry.profile_name,
                entry.analysis_period,
                entry.setup_date,
                entry.entry_price,
                entry.target_pct,
                int(
                    entry.success
                ),
                entry.days_to_target,
                entry.max_gain_pct,
                entry.max_drawdown_pct
            )
        )

        connection.commit()

        connection.close()

    def delete_for(
        self,
        symbol: str,
        profile_name: str,
        analysis_period: str
    ):

        connection = sqlite3.connect(
            self._database_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM historical_setups

            WHERE symbol = ?
            AND profile_name = ?
            AND analysis_period = ?
            """,
            (
                symbol.upper(),
                profile_name,
                analysis_period
            )
        )

        connection.commit()

        connection.close()

    def load_by_symbol(
        self,
        symbol: str,
        profile_name: str = "balanced",
        analysis_period: str = "1y"
    ) -> list[HistoricalSetupEntry]:

        connection = sqlite3.connect(
            self._database_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT

                symbol,
                profile_name,
                analysis_period,
                setup_date,
                entry_price,
                target_pct,
                success,
                days_to_target,
                max_gain_pct,
                max_drawdown_pct

            FROM historical_setups

            WHERE symbol = ?
            AND profile_name = ?
            AND analysis_period = ?

            ORDER BY setup_date DESC
            """,
            (
                symbol.upper(),
                profile_name,
                analysis_period
            )
        )

        rows = cursor.fetchall()

        connection.close()

        return [
            HistoricalSetupEntry(
                symbol=row[0],
                profile_name=row[1],
                analysis_period=row[2],
                setup_date=row[3],
                entry_price=row[4],
                target_pct=row[5],
                success=bool(
                    row[6]
                ),
                days_to_target=row[7],
                max_gain_pct=row[8],
                max_drawdown_pct=row[9]
            )
            for row in rows
        ]
