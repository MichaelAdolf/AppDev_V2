import sqlite3

from stockmind.domain.history.fundamental_data_entry import (
    FundamentalDataEntry
)


class FundamentalDataRepository:

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
            DROP TABLE IF EXISTS
            fundamental_data
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS fundamental_data (

                symbol TEXT NOT NULL PRIMARY KEY,

                company_name TEXT,

                sector TEXT,

                industry TEXT,

                market_cap REAL,

                trailing_pe REAL,

                forward_pe REAL,

                profit_margins REAL,

                revenue_growth REAL,

                recommendation_key TEXT,

                target_mean_price REAL,

                current_price REAL
            )
            """
        )

        connection.commit()

        connection.close()

    def save(
        self,
        entry: FundamentalDataEntry
    ):

        connection = sqlite3.connect(
            self._database_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT OR REPLACE INTO fundamental_data
            (
                symbol,
                company_name,
                sector,
                industry,
                market_cap,
                trailing_pe,
                forward_pe,
                profit_margins,
                revenue_growth,
                recommendation_key,
                target_mean_price,
                current_price
            )
            VALUES
            (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
            """,
            (
                entry.symbol,
                entry.company_name,
                entry.sector,
                entry.industry,
                entry.market_cap,
                entry.trailing_pe,
                entry.forward_pe,
                entry.profit_margins,
                entry.revenue_growth,
                entry.recommendation_key,
                entry.target_mean_price,
                entry.current_price
            )
        )

        connection.commit()

        connection.close()

    def load(
        self,
        symbol: str
    ) -> FundamentalDataEntry | None:

        connection = sqlite3.connect(
            self._database_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT

                symbol,
                company_name,
                sector,
                industry,
                market_cap,
                trailing_pe,
                forward_pe,
                profit_margins,
                revenue_growth,
                recommendation_key,
                target_mean_price,
                current_price

            FROM fundamental_data

            WHERE symbol = ?
            """,
            (symbol,)
        )

        row = cursor.fetchone()

        connection.close()

        if row is None:

            return None

        return FundamentalDataEntry(
            symbol=row[0],
            company_name=row[1],
            sector=row[2],
            industry=row[3],
            market_cap=row[4],
            trailing_pe=row[5],
            forward_pe=row[6],
            profit_margins=row[7],
            revenue_growth=row[8],
            recommendation_key=row[9],
            target_mean_price=row[10],
            current_price=row[11]
        )