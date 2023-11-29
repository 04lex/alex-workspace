from flask import Flask, request, jsonify
import sqlite3
import random
import string
import time

app = Flask(__name__)

def generate_token():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))

@app.route("/autentificare", methods=["POST"])
def autentificare():
    data = request.get_json()
    numar_cont = data["numar_cont"]
    parola = data["parola"]

    conn = sqlite3.connect("baza_de_date_clienti.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, nume, prenume FROM clienti WHERE numar_cont = ? AND parola = ?",
                   (numar_cont, parola))
    utilizator = cursor.fetchone()

    if utilizator:
        token = generate_token()
        cursor.execute("UPDATE clienti SET token = ? WHERE id = ?", (token, utilizator[0]))
        conn.commit()
        conn.close()
        return jsonify({"mesaj": f"Autentificare reusita, bine ati venit, {utilizator[1]} {utilizator[2]}!", "token": token})
    else:
        conn.close()
        return jsonify({"eroare": "Autentificare nereusita. Numarul de cont sau parola gresita."}), 401

@app.route("/actiune", methods=["GET"])
def actiune():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"eroare": "Token lipsă."}), 401

    conn = sqlite3.connect("baza_de_date_clienti.db")
    cursor = conn.cursor()

    cursor.execute("SELECT nume, prenume FROM clienti WHERE token = ?", (token,))
    utilizator = cursor.fetchone()

    if utilizator:
        conn.close()
        return jsonify({"mesaj": f"Actiune reusita, bine ati venit, {utilizator[0]} {utilizator[1]}!"})
    else:
        conn.close()
        return jsonify({"eroare": "Acces interzis. Token nevalid."}), 401

if __name__ == "__main__":
    app.run(debug=True)
