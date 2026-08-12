import sqlite3

from stockmind.domain.history.analysis_history_entry import ( AnalysisHistoryEntry )

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

    def save(
            self,
            entry: AnalysisHistoryEntry
    ):
        connection= sqlite3.connect(
            self._database_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO analysis_history
            (
                analysis_date,
                symbol,
                profile_name,
                opportunity_score,
                confidence,
                historical_success_rate,
                risk_level,
                signal
            )         
            VALUES
            (
            ?,?,?,?,?,?,?,?
            )   
            """
            (
                entry.analysis_date,
                entry.symbol,
                entry.profile_name,
                entry.opportunity_score,
                entry.confidence,
                entry.historical_success_rate,
                entry.risk_level,
                entry.signal
            )
        )

        connection.commit()

        connection.close()

    def load_by_symbol(
        self,
        symbol: str
    ) -> list[AnalysisHistoryEntry]:
        ct(
            self._database_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT

                analysis_date,
                symbol,
                profile_name,
                opportunity_score,
                confidence,
                historical_success_rate,
                risk_level,
                signal

            FROM analysis_history

            WHERE symbol = ?

            ORDER BY analysis_date
            """,
            (symbol,)
        )

        rows = cursor.fetchall()

        connection.close()

        return [
            AnalysisHistoryEntry(
                analysis_date=row[0],
                symbol=row[1],
                profile_name=row[2],
                opportunity_score=row[3],
                confidence=row[4],
                historical_success_rate=row[5],
                risk_level=row[6],
                signal=row[7]
            )
            for row in rows
        ]


