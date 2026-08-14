def _initialize(
    self
):

    connection = sqlite3.connect(
        self._database_path
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS historical_setups (

            symbol TEXT,

            setup_date TEXT,

            entry_price REAL,

            target_pct REAL,

            success INTEGER,

            days_to_target INTEGER,

            max_gain_pct REAL,

            max_drawdown_pct REAL
        )
        """
    )

    connection.commit()

    connection.close()
``
