import sqlite3

conn = sqlite3.connect("hokus.db")

# vytvoření kurzoru, který nám umoňuje navigaci po databázi a vkládání příkazů
cursor = conn.cursor()

# zápis do databáze
cursor.execute(
    "INSERT INTO houses (color) VALUES ('blue');"
)

conn.commit()

# uzavření spojení s databází
conn.close()