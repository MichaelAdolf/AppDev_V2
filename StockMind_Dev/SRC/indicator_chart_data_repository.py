import sqlite3

from stockmind.domain.history.indicator_chart_point import (
    IndicatorChartPoint
)

from stockmind.shared.config.settings import Settings

class IndicatorChartDataRepository:

    def __init__(
        self,
        database_path: str | None = None
    ):
        settings = Settings.load()

        self._database_path = database_path or settings.database_path

        self._initialize()

    def _initialize(
        self
    ):

        connection = sqlite3.connect(
            self._database_path
        )

        cursor = connection.cursor()

        #
        # Entwicklung:
        # Tabelle neu erstellen
        #

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS indicator_chart_data (

                symbol TEXT NOT NULL,

                trading_date TEXT NOT NULL,

                rsi_14 REAL,

                macd REAL,

                macd_signal REAL,

                macd_histogram REAL,

                adx REAL,

                plus_di REAL,

                minus_di REAL,

                stoch_k REAL,

                stoch_d REAL,

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
        points: list[IndicatorChartPoint]
    ):

        connection = sqlite3.connect(
            self._database_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM indicator_chart_data
            WHERE symbol = ?
            """,
            (symbol,)
        )

        for point in points:

            cursor.execute(
                """
                INSERT INTO
                indicator_chart_data
                (
                    symbol,
                    trading_date,

                    rsi_14,

                    macd,
                    macd_signal,
                    macd_histogram,

                    adx,
                    plus_di,
                    minus_di,

                    stoch_k,
                    stoch_d
                )
                VALUES
                (
                    ?, ?, ?,
                    ?, ?, ?,
                    ?, ?, ?,
                    ?, ?
                )
                """,
                (
                    point.symbol,
                    point.trading_date,

                    point.rsi_14,

                    point.macd,
                    point.macd_signal,
                    point.macd_histogram,

                    point.adx,
                    point.plus_di,
                    point.minus_di,

                    point.stoch_k,
                    point.stoch_d
                )
            )

        connection.commit()

        connection.close()

    def get_latest_date(self, symbol: str) -> str | None:
        connection = sqlite3.connect(self._database_path)
        row = connection.execute(
            "SELECT MAX(trading_date) FROM indicator_chart_data WHERE symbol = ?",
            (symbol.upper(),),
        ).fetchone()
        connection.close()
        return row[0] if row else None

    def upsert_points(self, points: list[IndicatorChartPoint]):
        if not points:
            return
        connection = sqlite3.connect(self._database_path)
        connection.executemany(
            """INSERT OR REPLACE INTO indicator_chart_data
               (symbol,trading_date,rsi_14,macd,macd_signal,macd_histogram,adx,plus_di,minus_di,stoch_k,stoch_d)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            [(p.symbol,p.trading_date,p.rsi_14,p.macd,p.macd_signal,p.macd_histogram,p.adx,p.plus_di,p.minus_di,p.stoch_k,p.stoch_d) for p in points],
        )
        connection.commit(); connection.close()

    def load_by_symbol(
        self,
        symbol: str
    ) -> list[IndicatorChartPoint]:

        connection = sqlite3.connect(
            self._database_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT

                symbol,
                trading_date,

                rsi_14,

                macd,
                macd_signal,
                macd_histogram,

                adx,
                plus_di,
                minus_di,

                stoch_k,
                stoch_d

            FROM indicator_chart_data

            WHERE symbol = ?

            ORDER BY trading_date
            """,
            (symbol,)
        )

        rows = cursor.fetchall()

        connection.close()

        return [

            IndicatorChartPoint(

                symbol=row[0],
                trading_date=row[1],

                rsi_14=row[2],

                macd=row[3],
                macd_signal=row[4],
                macd_histogram=row[5],

                adx=row[6],
                plus_di=row[7],
                minus_di=row[8],

                stoch_k=row[9],
                stoch_d=row[10]
            )

            for row in rows
        ]