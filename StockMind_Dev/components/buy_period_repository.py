import sqlite3

from stockmind.domain.history.buy_period_entry import BuyPeriodEntry
from stockmind.shared.config.settings import Settings


class BuyPeriodRepository:
    def __init__(self, database_path: str | None = None):
        settings = Settings.load()
        self._database_path = database_path or settings.database_path
        self._initialize()

    def _connect(self):
        return sqlite3.connect(self._database_path)

    def _initialize(self):
        connection = self._connect()
        try:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS buy_periods (
                    symbol TEXT NOT NULL,
                    profile_name TEXT NOT NULL,
                    analysis_period TEXT NOT NULL,
                    start_date TEXT NOT NULL,
                    end_date TEXT NOT NULL,
                    calendar_duration_days INTEGER NOT NULL,
                    buy_signal_count INTEGER NOT NULL,
                    gap_days_total INTEGER NOT NULL,
                    largest_gap_days INTEGER NOT NULL,
                    entry_price REAL NOT NULL,
                    target_pct REAL NOT NULL,
                    outcome TEXT NOT NULL,
                    target_hit INTEGER NOT NULL,
                    days_to_target INTEGER,
                    window_end_date TEXT,
                    window_end_return_pct REAL,
                    max_gain_pct REAL,
                    max_drawdown_pct REAL,
                    is_complete INTEGER NOT NULL,
                    PRIMARY KEY (
                        symbol,
                        profile_name,
                        analysis_period,
                        start_date
                    )
                )
                """
            )
            connection.commit()
        finally:
            connection.close()

    def replace_for(
        self,
        symbol: str,
        profile_name: str,
        analysis_period: str,
        periods: list[BuyPeriodEntry],
    ):
        connection = self._connect()
        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                DELETE FROM buy_periods
                WHERE symbol = ?
                AND profile_name = ?
                AND analysis_period = ?
                """,
                (symbol.upper(), profile_name, analysis_period),
            )
            cursor.executemany(
                """
                INSERT INTO buy_periods (
                    symbol, profile_name, analysis_period,
                    start_date, end_date, calendar_duration_days,
                    buy_signal_count, gap_days_total, largest_gap_days,
                    entry_price, target_pct, outcome, target_hit,
                    days_to_target, window_end_date, window_end_return_pct,
                    max_gain_pct, max_drawdown_pct, is_complete
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                [self._to_row(period) for period in periods],
            )
            connection.commit()
        finally:
            connection.close()

    def load_by_symbol(
        self,
        symbol: str,
        profile_name: str = "balanced",
        analysis_period: str = "5y",
    ) -> list[BuyPeriodEntry]:
        connection = self._connect()
        try:
            rows = connection.execute(
                """
                SELECT
                    symbol, profile_name, analysis_period,
                    start_date, end_date, calendar_duration_days,
                    buy_signal_count, gap_days_total, largest_gap_days,
                    entry_price, target_pct, outcome, target_hit,
                    days_to_target, window_end_date, window_end_return_pct,
                    max_gain_pct, max_drawdown_pct, is_complete
                FROM buy_periods
                WHERE symbol = ?
                AND profile_name = ?
                AND analysis_period = ?
                ORDER BY start_date DESC
                """,
                (symbol.upper(), profile_name, analysis_period),
            ).fetchall()
        finally:
            connection.close()
        return [self._from_row(row) for row in rows]

    def _to_row(self, period: BuyPeriodEntry) -> tuple:
        return (
            period.symbol, period.profile_name, period.analysis_period,
            period.start_date, period.end_date, period.calendar_duration_days,
            period.buy_signal_count, period.gap_days_total,
            period.largest_gap_days, period.entry_price, period.target_pct,
            period.outcome, int(period.target_hit), period.days_to_target,
            period.window_end_date, period.window_end_return_pct,
            period.max_gain_pct, period.max_drawdown_pct,
            int(period.is_complete),
        )

    def _from_row(self, row) -> BuyPeriodEntry:
        return BuyPeriodEntry(
            symbol=row[0], profile_name=row[1], analysis_period=row[2],
            start_date=row[3], end_date=row[4],
            calendar_duration_days=row[5], buy_signal_count=row[6],
            gap_days_total=row[7], largest_gap_days=row[8],
            entry_price=row[9], target_pct=row[10], outcome=row[11],
            target_hit=bool(row[12]), days_to_target=row[13],
            window_end_date=row[14], window_end_return_pct=row[15],
            max_gain_pct=row[16], max_drawdown_pct=row[17],
            is_complete=bool(row[18]),
        )
