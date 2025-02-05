import sqlite3

# Vytvoření nebo připojení k databázi
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Vytvoření tabulky
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

# Funkce pro vložení dat do tabulky
def insert_user(name, age):
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    conn.commit()

# Funkce pro načtení dat z tabulky
def fetch_users():
    cursor.execute('SELECT * FROM users')
    return cursor.fetchall()

# Vložení dat
insert_user('Alice', 30)
insert_user('Bob', 25)

# Načtení a výpis dat
users = fetch_users()
for user in users:
    print(f"ID: {user[0]}, Jméno: {user[1]}, Věk: {user[2]}")

# Uzavření připojení
conn.close()
