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
