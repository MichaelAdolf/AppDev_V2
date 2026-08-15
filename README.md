import sqlite3

conne*tion = sqlite3.connect(
    "stock*ind.db"
)

cursor = connection.cur*or()

cursor.execute(
    """
    *ELECT COUNT(*)
    FROM historical*setups
    """
)

print(
    curso*.fetchone()
)

connection.close()
*
