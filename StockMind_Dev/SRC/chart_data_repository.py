import sqlite3

from stockmind.domain.history.chart_point import ChartPoint
from stockmind.shared.config.settings import Settings


class ChartDataRepository:
    EXTRA_COLUMNS = {
        "open_price": "REAL",
        "high_price": "REAL",
        "low_price": "REAL",
    }

    def __init__(self, database_path: str | None = None):
        self._database_path = database_path or Settings.load().database_path
        self._initialize()

    def _connect(self):
        return sqlite3.connect(self._database_path)

    def _initialize(self):
        connection = self._connect()
        try:
            connection.execute("""
                CREATE TABLE IF NOT EXISTS chart_data (
                    symbol TEXT NOT NULL,
                    trading_date TEXT NOT NULL,
                    close_price REAL,
                    bollinger_upper REAL,
                    bollinger_middle REAL,
                    bollinger_lower REAL,
                    open_price REAL,
                    high_price REAL,
                    low_price REAL,
                    PRIMARY KEY (symbol, trading_date)
                )
            """)
            existing = {
                row[1]
                for row in connection.execute(
                    "PRAGMA table_info(chart_data)"
                ).fetchall()
            }
            for name, data_type in self.EXTRA_COLUMNS.items():
                if name not in existing:
                    connection.execute(
                        f"ALTER TABLE chart_data ADD COLUMN {name} {data_type}"
                    )
            connection.commit()
        finally:
            connection.close()

    def replace_for_symbol(self, symbol: str, points: list[ChartPoint]):
        connection = self._connect()
        try:
            connection.execute(
                "DELETE FROM chart_data WHERE symbol = ?",
                (symbol.upper(),),
            )
            self._write_points(connection, points)
            connection.commit()
        finally:
            connection.close()

    def upsert_points(self, points: list[ChartPoint]):
        if not points:
            return
        connection = self._connect()
        try:
            self._write_points(connection, points)
            connection.commit()
        finally:
            connection.close()

    def _write_points(self, connection, points):
        connection.executemany("""
            INSERT OR REPLACE INTO chart_data (
                symbol, trading_date, close_price,
                bollinger_upper, bollinger_middle, bollinger_lower,
                open_price, high_price, low_price
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, [(
            point.symbol.upper(), point.trading_date, point.close_price,
            point.bollinger_upper, point.bollinger_middle,
            point.bollinger_lower, point.open_price,
            point.high_price, point.low_price,
        ) for point in points])

    def get_latest_date(self, symbol: str) -> str | None:
        connection = self._connect()
        try:
            row = connection.execute(
                "SELECT MAX(trading_date) FROM chart_data WHERE symbol = ?",
                (symbol.upper(),),
            ).fetchone()
        finally:
            connection.close()
        return row[0] if row else None

    def load_by_symbol(self, symbol: str) -> list[ChartPoint]:
        connection = self._connect()
        try:
            rows = connection.execute("""
                SELECT symbol, trading_date, close_price,
                       bollinger_upper, bollinger_middle, bollinger_lower,
                       open_price, high_price, low_price
                FROM chart_data
                WHERE symbol = ?
                ORDER BY trading_date
            """, (symbol.upper(),)).fetchall()
        finally:
            connection.close()
        return [ChartPoint(*row) for row in rows]

    def has_complete_ohlc(self, symbol: str) -> bool:
        connection = self._connect()
        try:
            row = connection.execute("""
                SELECT COUNT(*),
                       SUM(CASE WHEN open_price IS NOT NULL
                                     AND high_price IS NOT NULL
                                     AND low_price IS NOT NULL
                                THEN 1 ELSE 0 END)
                FROM chart_data
                WHERE symbol = ?
            """, (symbol.upper(),)).fetchone()
        finally:
            connection.close()
        total, complete = row or (0, 0)
        return total > 0 and total == complete
