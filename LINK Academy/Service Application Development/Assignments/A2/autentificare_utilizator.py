import sqlite3
import random
import string
import time

def generate_token():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))

def autentificare(numar_cont, parola):
    conn = sqlite3.connect("baza_de_data_clienti.db")
    cursor = conn.cursor()

    cursor.execute("SELECT nume, prenume, token FROM clienti WHERE numar_cont = ? AND parola = ?",
                    (numar_cont, parola))

    utilizator = cursor.fetchone()

    if utilizator:
        token = generate_token()
        expirate_token = int(time.time()) + 45 # valabil 45 secunde
        cursor.execute("UPDATE clienti SET token = ? WHERE numar_cont = ?", (token, numar_cont))
        conn.commit()
        conn.close()
        return f"Ai intrat in cont! Bine ai venit, {utilizator[0]} {utilizator[1]}. Tokenul tau este: {token}"
    else:
        conn.close()
        return "Eroare: Autentificare nereusita. Numarul de cont sau parola incorecte."

# functionalitate:
numar_cont_input = int(input("Introduceti numarul de cont: \n"))
parola_input = input("Introduceti parola: \n")

rezultat = autentificare(numar_cont_input, parola_input)
print(rezultat)