import sqlite3

conn = sqlite3.connect("baza_de_data_clienti.db")
cursor = conn.cursor()


# tabel pentru clienti
cursor.execute('''CREATE TABLE IF NOT EXISTS clienti(
                id INTEGER PRIMARY KEY,
                nume TEXT,
                prenume TEXT,
                numar_cont INTEGER,
                parola TEXT,
                token TEXT)''')

# trei utilizatori arbitrari
cursor.execute("INSERT INTO clienti (nume, prenume, numar_cont, parola) VALUES (?, ?, ?, ?)",
                ("Nume1", "Prenume1", "12345", "parola1"))
cursor.execute("INSERT INTO clienti (nume, prenume, numar_cont, parola) VALUES (?, ?, ?, ?)",
                ("Nume2", "Prenume2", "67890", "parola2"))
cursor.execute("INSERT INTO clienti (nume, prenume, numar_cont, parola) VALUES (?, ?, ?, ?)",
                ("Nume3", "Prenume3", "00112", "parola3"))






conn.commit()
conn.close()