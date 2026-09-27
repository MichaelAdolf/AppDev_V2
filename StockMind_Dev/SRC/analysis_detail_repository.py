import sqlite3

from stockmind.domain.history.analysis_detail_entry import(
    AnalysisDetailEntry
)

from stockmind.shared.config.settings import Settings


class AnalysisDetailRepository:

    def __init__(
        self,
        database_path: str | None = None
    ):
        settings = Settings.load()
        
        self._database_path = settings.database_path

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
            CREATE TABLE IF NOT EXISTS analysis_details (

                symbol TEXT NOT NULL,

                profile_name TEXT NOT NULL,

                summary TEXT,

                strengths TEXT,

                weaknesses TEXT,

                PRIMARY KEY (
                    symbol,
                    profile_name
                )
            )
            """
        )

        connection.commit()

        connection.close()

    def load(
            self,
            symbol: str,
            profile_name: str
    ) -> AnalysisDetailEntry | None:

        connection = sqlite3.connect(
            self._database_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT

                symbol,
                profile_name,
                summary,
                strengths,
                weaknesses

            FROM analysis_details

            WHERE symbol = ?
            AND profile_name = ?
            """,
            (
                symbol,
                profile_name
            )
        )

        row = cursor.fetchone()

        connection.close()

        if row is None:

            return None

        return AnalysisDetailEntry(
            symbol=row[0],
            profile_name=row[1],
            summary=row[2],
            strengths=row[3],
            weaknesses=row[4]
        )

    def save(
            self,
            entry: AnalysisDetailEntry
    ):
        connection = sqlite3.connect(
            self._database_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT OR REPLACE INTO
            analysis_details
            (
                symbol,
                profile_name,
                summary,
                strengths,
                weaknesses
            )
            VALUES
            (
                ?, ?, ?, ?, ?
            )
            """,
            (
                entry.symbol,
                entry.profile_name,
                entry.summary,
                entry.strengths,
                entry.weaknesses
            )
        )

        connection.commit()
        
        connection.close()