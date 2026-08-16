import sqlite3


def main():

    connection = sqlite3.connect(
        "stockmind.db"
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            symbol,
            profile_name,
            analysis_period,
            COUNT(1)
        FROM historical_setups
        GROUP BY
            symbol,
            profile_name,
            analysis_period
        ORDER BY
            symbol,
            profile_name,
            analysis_period
        """
    )

    rows = cursor.fetchall()

    for row in rows:

        print(
            f"Symbol={row[0]} | "
            f"Profile={row[1]} | "
            f"Period={row[2]} | "
            f"Count={row[3]}"
        )

    connection.close()


if __name__ == "__main__":

    main()
