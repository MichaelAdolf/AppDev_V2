import sqlite3

from stockmind.domain.history.historical_outcome import HistoricalOutcome
from stockmind.domain.history.historical_setup_entry import HistoricalSetupEntry
from stockmind.shared.config.settings import Settings


class HistoricalSetupRepository:
    EXTRA_COLUMNS = {
        "window_start_date": "TEXT",
        "window_end_date": "TEXT",
        "window_end_return_pct": "REAL",
        "outcome": "TEXT",
        "is_complete": "INTEGER DEFAULT 0",
    }

    def __init__(self, database_path: str | None = None):
        settings = Settings.load()
        self._database_path = (
            database_path
            if database_path is not None
            else settings.database_path
        )
        self._initialize()

    def _connect(self):
        return sqlite3.connect(self._database_path)

    def _initialize(self):
        connection = self._connect()
        try:
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
                    max_drawdown_pct REAL,
                    window_start_date TEXT,
                    window_end_date TEXT,
                    window_end_return_pct REAL,
                    outcome TEXT,
                    is_complete INTEGER DEFAULT 0
                )
                """
            )
            self._migrate_missing_columns(cursor)
            connection.commit()
        finally:
            connection.close()

    def _migrate_missing_columns(self, cursor):
        cursor.execute("PRAGMA table_info(historical_setups)")
        existing_columns = {row[1] for row in cursor.fetchall()}
        for column_name, column_type in self.EXTRA_COLUMNS.items():
            if column_name not in existing_columns:
                cursor.execute(
                    f"ALTER TABLE historical_setups "
                    f"ADD COLUMN {column_name} {column_type}"
                )

    def save(self, entry: HistoricalSetupEntry):
        connection = self._connect()
        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                INSERT INTO historical_setups (
                    symbol,
                    profile_name,
                    analysis_period,
                    setup_date,
                    entry_price,
                    target_pct,
                    success,
                    days_to_target,
                    max_gain_pct,
                    max_drawdown_pct,
                    window_start_date,
                    window_end_date,
                    window_end_return_pct,
                    outcome,
                    is_complete
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    entry.symbol,
                    entry.profile_name,
                    entry.analysis_period,
                    entry.setup_date,
                    entry.entry_price,
                    entry.target_pct,
                    int(entry.success),
                    entry.days_to_target,
                    entry.max_gain_pct,
                    entry.max_drawdown_pct,
                    entry.window_start_date,
                    entry.window_end_date,
                    entry.window_end_return_pct,
                    entry.outcome,
                    int(entry.is_complete),
                ),
            )
            connection.commit()
        finally:
            connection.close()

    def delete_for(
        self,
        symbol: str,
        profile_name: str,
        analysis_period: str,
    ):
        connection = self._connect()
        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                DELETE FROM historical_setups
                WHERE symbol = ?
                AND profile_name = ?
                AND analysis_period = ?
                """,
                (symbol.upper(), profile_name, analysis_period),
            )
            connection.commit()
        finally:
            connection.close()

    def load_by_symbol(
        self,
        symbol: str,
        profile_name: str = "balanced",
        analysis_period: str = "1y",
    ) -> list[HistoricalSetupEntry]:
        connection = self._connect()
        try:
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
                    max_drawdown_pct,
                    window_start_date,
                    window_end_date,
                    window_end_return_pct,
                    outcome,
                    is_complete
                FROM historical_setups
                WHERE symbol = ?
                AND profile_name = ?
                AND analysis_period = ?
                ORDER BY setup_date DESC
                """,
                (symbol.upper(), profile_name, analysis_period),
            )
            rows = cursor.fetchall()
        finally:
            connection.close()

        return [
            HistoricalSetupEntry(
                symbol=row[0],
                profile_name=row[1],
                analysis_period=row[2],
                setup_date=row[3],
                entry_price=row[4],
                target_pct=row[5],
                success=bool(row[6]),
                days_to_target=row[7],
                max_gain_pct=row[8],
                max_drawdown_pct=row[9],
                window_start_date=row[10] or row[3],
                window_end_date=row[11],
                window_end_return_pct=row[12],
                outcome=(
                    row[13]
                    or (
                        HistoricalOutcome.TARGET_HIT.value
                        if bool(row[6])
                        else HistoricalOutcome.INCOMPLETE_WINDOW.value
                    )
                ),
                is_complete=bool(row[14]),
            )
            for row in rows
        ]
