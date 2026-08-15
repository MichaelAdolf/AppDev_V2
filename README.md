import sqlite3


def main():

    connection = sqlite3.connect(
        "stockmind.db"
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        DROP TABLE IF EXISTS historical_setups
        """
    )

    connection.commit()

    connection.close()

    print(
        "historical_setups table reset."
    )


if __name__ == "__main__":
    main()
``
