connection = sqlite3.connect(
    self._database_path
)

cursor = connection.cursor()

cursor.execute(
    """
    INSERT INTO historical_setups
    (
        symbol,
        setup_date,
        entry_price,
        target_pct,
        success,
        days_to_target,
        max_gain_pct,
        max_drawdown_pct
    )
    VALUES
    (
        ?, ?, ?, ?, ?, ?, ?, ?
    )
    """,
    (
        entry.symbol,
        entry.setup_date,
        entry.entry_price,
        entry.target_pct,
        int(entry.success),
        entry.days_to_target,
        entry.max_gain_pct,
        entry.max_drawdown_pct
    )
)

connection.commit()

connection.close()
