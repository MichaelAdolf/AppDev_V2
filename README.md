import sqlite3

from stockmind.domain.history.analysis_history_entry import (
    AnalysisHistoryEntry
)


class AnalysisHistoryRepository:

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
            CREATE TABLE IF NOT EXISTS analysis_history (

                analysis_date TEXT,

                symbol TEXT,

                profile_name TEXT,

                opportunity_score REAL,

                confidence REAL,

                historical_success_rate REAL,

                risk_level TEXT,

                signal TEXT
            )
            """
        )

        connection.commit()

        connection.close()
