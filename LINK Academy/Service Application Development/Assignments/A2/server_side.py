from flask import Flask, request, jsonify
import sqlite3
import secrets
import time

app = Flask(__name__)

# generez token
def generate_token():
    return secrets.token_hex(16)

# autentificare token
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    numar_cont = data['numar_cont']
    parola = data['parola']

    # db conn
    conn = sqlite3.connect('db_server.db')
    cursor = conn.cursor()

    # check auth
    cursor.execute('SELECT * FROM utilizatori WHERE numar_cont=? AND parola=?', (numar_cont, parola))
    user = cursor.fetchone()
    conn.close()

    if user:
        token = generate_token()
        # update token in db
        conn = sqlite3.connect('db_server.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE utilizatori SET token=? WHERE numar_cont=?', (token, numar_cont))
        conn.commit()
        conn.close()
        return jsonify({'token': token}), 200
    else:
        return 'Autentificare nereusita', 401
    

# afisare date pentru token
@app.route('/cont', methods=['GET'])
def get_cont_details():
    token = request.headers.get('Authorization')
    if not token:
        return 'Token invalid', 401
    
    # verificare token in db
    conn = sqlite3.connect('db_server.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM utilizatori WHERE token=?', (token,))
    user = cursor.fetchone()
    conn.close()

    if user:
        # afisare date
        numar_cont = user[1]

        return jsonify({'numar_cont': numar_cont}), 200
    else:
        return 'Acces neautorizat', 403
    
if __name__ == '__main__':
    app.run(debug=True)