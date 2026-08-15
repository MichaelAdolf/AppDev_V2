AttributeError: 'IndicatorChartPoint' object has no attribute 'adx'
Traceback:

File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\ui\streamlit_app.py", line 90, in <module>
    render_stock_detail(
    ~~~~~~~~~~~~~~~~~~~^
        profile_name=profile,
        ^^^^^^^^^^^^^^^^^^^^^
        symbol=selected_symbol
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\ui\components\stock_detail_view.py", line 362, in render
    render_adx_chart(
    ~~~~~~~~~~~~~~~~^
        dashboard.symbol
        ^^^^^^^^^^^^^^^^
    )
    ^
File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\ui\components\indicator_charts.py", line 183, in render_adx_chart
    point.adximport sqlite3

from stockmind.domain.history.indicator_chart_point import (
    IndicatorChartPoint
)


class IndicatorChartDataRepository:

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

        #
        # Entwicklung:
        # Tabelle neu erstellen
        #

        cursor.execute(
            """
            DROP TABLE IF EXISTS
            indicator_chart_data
            """
        )

        cursor.execute(
            """
            CREATE TABLE indicator_chart_data (

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
