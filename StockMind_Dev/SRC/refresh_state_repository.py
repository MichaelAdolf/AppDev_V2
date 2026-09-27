import sqlite3
from datetime import datetime
from stockmind.shared.config.settings import Settings


class RefreshStateRepository:
    def __init__(self, database_path: str | None = None):
        self._database_path = database_path or Settings.load().database_path
        self._initialize()

    def _connect(self):
        return sqlite3.connect(self._database_path)

    def _initialize(self):
        connection = self._connect()
        connection.execute("""
            CREATE TABLE IF NOT EXISTS refresh_state (
                symbol TEXT PRIMARY KEY,
                bootstrap_complete INTEGER NOT NULL DEFAULT 0,
                last_success_at TEXT,
                last_mode TEXT,
                last_error TEXT
            )
        """)
        connection.commit(); connection.close()

    def is_bootstrapped(self, symbol: str) -> bool:
        connection=self._connect();row=connection.execute(
            "SELECT bootstrap_complete FROM refresh_state WHERE symbol=?",
            (symbol.upper(),),
        ).fetchone();connection.close()
        return bool(row[0]) if row else False

    def mark_success(self, symbol: str, mode: str):
        connection=self._connect();connection.execute("""
            INSERT INTO refresh_state(symbol,bootstrap_complete,last_success_at,last_mode,last_error)
            VALUES(?,1,?,?,NULL)
            ON CONFLICT(symbol) DO UPDATE SET
                bootstrap_complete=1,last_success_at=excluded.last_success_at,
                last_mode=excluded.last_mode,last_error=NULL
        """,(symbol.upper(),datetime.now().isoformat(timespec="seconds"),mode));connection.commit();connection.close()

    def mark_error(self, symbol: str, mode: str, error: str):
        connection=self._connect();connection.execute("""
            INSERT INTO refresh_state(symbol,bootstrap_complete,last_success_at,last_mode,last_error)
            VALUES(?,0,NULL,?,?)
            ON CONFLICT(symbol) DO UPDATE SET last_mode=excluded.last_mode,last_error=excluded.last_error
        """,(symbol.upper(),mode,error));connection.commit();connection.close()
