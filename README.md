def load_by_symbol(
    self,
    symbol: str
) -> list```

Inhalt:

```python
connection = sqlite3.connect(
    self._database_path
)

cursor = connection.cursor()

cursor.execute(
    """
    SELECT

        symbol,
        setup_date,
        entry_price,
        target_pct,
        success,
        days_to_target,
        max_gain_pct,
        max_drawdown_pct

    FROM historical_setups

    WHERE symbol = ?

    ORDER BY setup_date DESC
    """,
    (symbol,)
)

rows = cursor.fetchall()

connection.close()

return [
    HistoricalSetupEntry(
        symbol=row[0],
        setup_date=row[1],
        entry_price=row[2],
        target_pct=row[3],
        success=bool(row[4]),
        days_to_target=row[5],
        max_gain_pct=row[6],
        max_drawdown_pct=row[7]
    )
    for row in rows
]
