    def load_by_symbol(
        self,
        symbol: str
    ) -> listconnection = sqlite3.connect(
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
