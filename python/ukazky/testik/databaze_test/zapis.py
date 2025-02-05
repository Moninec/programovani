import sqlite3

# vytvoření spojení s databází?
connection = sqlite3.connect("hokus.db")

# vytvoření kurzoru, který nám umoňuje navigaci po databázi a vkládání příkazů
cursor = connection.cursor()

input_color = input("Add house color: ")

# zápis do databáze
cursor.execute(
    "INSERT INTO houses (color) VALUES (?)", (input_color,)
)

#potvrzení vložení dat do databáze
connection.commit()

# výběr dat z databáze pomocí kurzoru+
cursor.execute("SELECT * FROM houses")
# fetchall() data získá a umožní nám je uložit pod proměnnou
# data se vrací jako list jednotlivých rows (řad) z databáze, kde data v řadě jsou v tuple 
# [(data za řady 1, další data z řady 1), (data z řady 2, další data z řady 2)]
rows = cursor.fetchall()

for row in rows:
    print(row)

# uzavření spojení s databází
connection.close()
