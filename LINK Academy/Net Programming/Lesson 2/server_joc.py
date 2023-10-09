import socket
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Refolosesc adresa 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind
server.bind(('127.0.0.1', 8007))
server.listen()

conn, address = server.accept()

alegeri = {"1": "Piatra", "2":"Hartie", "3":"Foarfeca"}
mesaj = 'Alegeti una din variantele: 1 - Piatra, 2 - Hartie, 3 - Foarfeca'

conn.send(bytes(mesaj, 'utf-8'))

alegere_client = conn.recv(1024).decode('utf-8')
print(alegere_client) # Din 1, 2, 3

alegere_server = random.choice(["1", "2", "3"])

# logica de business
mesaj_rezultat = ""

if alegere_client == alegere_server:
    mesaj_rezultat = "Egalitate"
elif alegere_client == "1":
    if alegere_server == "2":
        mesaj_rezultat = "Ai pierdut"
    else:
        mesaj_rezultat = "Ai castigat"
elif alegere_client == "2":
    if alegere_server == "3":
        mesaj_rezultat = "Ai pierdut"
    else:
        mesaj_rezultat = "Ai castigat"
elif alegere_client == "3":
    if alegere_server == "1":
        mesaj_rezultat = "Ai pierdut"
    else:
        mesaj_rezultat = "Ai castigat"

mesaj_rezultat += f', serverul a ales {alegeri[alegere_server]}, iar tu ai ales {alegeri[alegere_client]}'

conn.send(bytes(mesaj_rezultat, 'utf-8'))