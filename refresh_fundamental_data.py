import sqlite3

connection = sqlite3.connect(
    "stockmind.db"
)

cursor = connection.cursor()

cursor.execute(
    """
    SELECT *
    FROM fundamental_data
    """
)

rows = cursor.fetchall()

print(
    f"Anzahl Datensätze: {len(rows)}"
)

for row in rows[:3]:

    print(row)

connection.close()
