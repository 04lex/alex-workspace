import sqlite3

# Crearea bazei de date
conn = sqlite3.connect("baza_de_date_clienti.db")
cursor = conn.cursor()

# Crearea tabelului "clienti"
cursor.execute('''CREATE TABLE IF NOT EXISTS clienti (
                  id INTEGER PRIMARY KEY,
                  nume TEXT,
                  prenume TEXT,
                  numar_cont INTEGER,
                  parola TEXT,
                  token TEXT)''')

# Adăugarea a trei utilizatori arbitrari
cursor.execute("INSERT INTO clienti (nume, prenume, numar_cont, parola, token) VALUES (?, ?, ?, ?, ?)",
               ("John", "Doe", 12345, "parola1", ""))
cursor.execute("INSERT INTO clienti (nume, prenume, numar_cont, parola, token) VALUES (?, ?, ?, ?, ?)",
               ("Jane", "Smith", 67890, "parola2", ""))
cursor.execute("INSERT INTO clienti (nume, prenume, numar_cont, parola, token) VALUES (?, ?, ?, ?, ?)",
               ("Alice", "Johnson", 54321, "parola3", ""))

conn.commit()
conn.close()
