import sqlite3
from stockmind.domain.history.analysis_history_entry import AnalysisHistoryEntry
from stockmind.shared.config.settings import Settings


class AnalysisHistoryRepository:
    def __init__(self, database_path: str | None = None):
        settings = Settings.load()
        self._database_path = database_path or settings.database_path
        self._initialize()

    def _connect(self):
        return sqlite3.connect(self._database_path)

    def _initialize(self):
        connection = self._connect()
        connection.execute("""
            CREATE TABLE IF NOT EXISTS analysis_history (
                analysis_date TEXT, symbol TEXT, profile_name TEXT,
                opportunity_score REAL, confidence REAL,
                historical_success_rate REAL, risk_level TEXT, signal TEXT
            )
        """)
        connection.commit(); connection.close()

    def save(self, entry: AnalysisHistoryEntry):
        connection = self._connect()
        connection.execute("""
            INSERT INTO analysis_history (
                analysis_date, symbol, profile_name, opportunity_score,
                confidence, historical_success_rate, risk_level, signal
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            entry.analysis_date, entry.symbol, entry.profile_name,
            entry.opportunity_score, entry.confidence,
            entry.historical_success_rate, entry.risk_level, entry.signal,
        ))
        connection.commit(); connection.close()

    def load_by_symbol(
        self,
        symbol: str,
        profile_name: str | None = None,
    ) -> list[AnalysisHistoryEntry]:
        connection = self._connect()
        parameters = [symbol.upper()]
        profile_clause = ""
        if profile_name is not None:
            profile_clause = " AND profile_name = ?"
            parameters.append(profile_name)
        rows = connection.execute(f"""
            SELECT analysis_date, symbol, profile_name, opportunity_score,
                   confidence, historical_success_rate, risk_level, signal
            FROM analysis_history AS history
            WHERE symbol = ? {profile_clause}
              AND rowid = (
                  SELECT MAX(newest.rowid)
                  FROM analysis_history AS newest
                  WHERE newest.symbol = history.symbol
                    AND newest.profile_name = history.profile_name
                    AND newest.analysis_date = history.analysis_date
              )
            ORDER BY analysis_date
        """, parameters).fetchall()
        connection.close()
        return [AnalysisHistoryEntry(
            analysis_date=row[0], symbol=row[1], profile_name=row[2],
            opportunity_score=row[3], confidence=row[4],
            historical_success_rate=row[5], risk_level=row[6], signal=row[7],
        ) for row in rows]
