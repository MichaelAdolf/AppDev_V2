    def save(
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
