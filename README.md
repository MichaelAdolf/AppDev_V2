def _initialize(
    self
):

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
