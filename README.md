import sqlite3


def main():

    connection = sqlite3.connect(
        "stockmind.db"
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT COUNT(1)
        FROM historical_setups
        """
    )

    count = cursor.fetchone()[0]

    print(
        f"Historical setups found: {count}"
    )

    connection.close()


if __name__ == "__main__":

    main()
