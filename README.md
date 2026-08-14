import sqlite3

from stockmind.domain.history.chart_point import (
    ChartPoint
)


class ChartDataRepository:

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
            CREATE TABLE IF NOT EXISTS chart_data (

                symbol TEXT NOT NULL,

                trading_date TEXT NOT NULL,

                close_price REAL,

                bollinger_upper REAL,

                bollinger_middle REAL,

                bollinger_lower REAL,

                PRIMARY KEY (
                    symbol,
                    trading_date
                )
            )
            """
        )

        connection.commit()

        connection.close()

    def replace_for_symbol(
        self,
        symbol: str,
        points: list[ChartPoint]
    ):

        connection = sqlite3.connect(
            self._database_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM chart_data
            WHERE symbol = ?
            """,
            (symbol,)
        )

        for point in points:

            cursor.execute(
                """
                INSERT OR REPLACE INTO chart_data
                (
                    symbol,
                    trading_date,
                    close_price,
                    bollinger_upper,
                    bollinger_middle,
                    bollinger_lower
                )
                VALUES
                (
                    ?, ?, ?, ?, ?, ?
                )
                """,
                (
                    point.symbol,
                    point.trading_date,
                    point.close_price,
                    point.bollinger_upper,
                    point.bollinger_middle,
                    point.bollinger_lower
                )
            )

        connection.commit()

        connection.close()

    def load_by_symbol(
        self,
        symbol: str
    ) -> list[ChartPoint]:

        connection = sqlite3.connect(
            self._database_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                symbol,
                trading_date,
                close_price,
                bollinger_upper,
                bollinger_middle,
                bollinger_lower

            FROM chart_data

            WHERE symbol = ?

            ORDER BY trading_date
            """,
            (symbol,)
        )

        rows = cursor.fetchall()

        connection.close()

        return [
            ChartPoint(
                symbol=row[0],
                trading_date=row[1],
                close_price=row[2],
                bollinger_upper=row[3],
                bollinger_middle=row[4],
                bollinger_lower=row[5]
            )
            for row in rows
        ]
