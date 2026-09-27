import sqlite3

from stockmind.domain.history.latest_analysis_entry import LatestAnalysisEntry

from stockmind.shared.config.settings import Settings

class LatestAnalysisRepository:

    def __init__(
            self,
            database_path: str | None = None
    ):
        settings = Settings.load()

        self._database_path = settings.database_path

        self._initialize()

    def _initialize( self ):

        connection = sqlite3.connect(
            self._database_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS latest_analysis (

                symbol TEXT NOT NULL,

                profile_name TEXT NOT NULL,

                opportunity_score REAL,

                confidence REAL,

                historical_success_rate REAL,

                risk_level TEXT,

                signal TEXT,

                PRIMARY KEY (
                    symbol,
                    profile_name
                )
            )
            """
        )

        connection.commit()

        connection.close()


    def save(
            self,
            entry: LatestAnalysisEntry
    ):
        connection = sqlite3.connect(
            self._database_path
        )
        
        cursor = connection.cursor()
        
        cursor.execute(
            """
            INSERT OR REPLACE INTO latest_analysis 
            (
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
            ?, ?, ?, ?, ?, ?, ?
            )
            """,
            (
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

    def load_all(
        self,
        profile_name: str
    ) -> list[LatestAnalysisEntry]:

        connection = sqlite3.connect(
            self._database_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT

                symbol,
                profile_name,
                opportunity_score,
                confidence,
                historical_success_rate,
                risk_level,
                signal

            FROM latest_analysis

            WHERE profile_name = ?

            ORDER BY opportunity_score DESC
            """,
            (profile_name,)
        )

        rows = cursor.fetchall()

        connection.close()

        return [
            LatestAnalysisEntry(
                symbol=row[0],
                profile_name=row[1],
                opportunity_score=row[2],
                confidence=row[3],
                historical_success_rate=row[4],
                risk_level=row[5],
                signal=row[6]
            )
            for row in rows
        ]

        