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
