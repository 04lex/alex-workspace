import sqlite3
# import os

# cur_dir = os.path.dirname(os.path.abspath(__file__))
# cale_db = os.path.join(cur_dir, 'db_server.db')


conn = sqlite3.connect('db_server.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS utilizatori (
               id INTEGER PRIMARY KEY,
               numar_cont TEXT UNIQUE,
               nume TEXT,
               prenume TEXT,
               parola TEXT,
               token TEXT
                )''')

# users
utilizatori = [
    ('user1', 'Andrei', 'Marin', 'parola123', ''),
    ('user2', 'Ion', 'Pop', 'parola321', ''),
    ('n0trea11', 'Kyel', 'Selina', 'parola112', ''),
]

cursor.executemany('''INSERT INTO utilizatori (numar_cont, nume, prenume, parola, token) VALUES (?, ?, ?, ?, ?)''', utilizatori)

conn.commit()
conn.close()