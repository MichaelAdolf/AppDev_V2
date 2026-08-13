def _initializeconnection = sqlite3.connect(
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
