import socket
import random
import enum

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Refolosesc adresa 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Server bind
server.bind(('127.0.0.1', 8007))
server.listen()

conn, address = server.accept()

# enumar alegerile pentru joc intr-o clasa
class AlegeriJoc(enum.Enum):
    Piatra   = 1
    Hartie   = 2
    Foarfeca = 3
    Soparla  = 4
    Spock    = 5
# un dictionar cu key-uri dictionar pentru 'castigatori'
logica_de_business = {
    AlegeriJoc.Piatra: (AlegeriJoc.Foarfeca, AlegeriJoc.Soparla),
    AlegeriJoc.Hartie: (AlegeriJoc.Spock, AlegeriJoc.Piatra),
    AlegeriJoc.Foarfeca: (AlegeriJoc.Hartie, AlegeriJoc.Soparla),
    AlegeriJoc.Soparla: (AlegeriJoc.Hartie, AlegeriJoc.Spock),
    AlegeriJoc.Spock: (AlegeriJoc.Piatra, AlegeriJoc.Foarfeca),
}
# mesajul fara variante
mesaj = "Alegeti una din variante:"
# iterez prin alegerile din dictionar si le adaug in mesaj
for alegere in AlegeriJoc:
    mesaj += ("\n" + str(alegere.value) + " - " + alegere.name)

# trimite server-ului client alegerile de joc
conn.send(bytes(mesaj, 'utf-8'))

alegere_client = conn.recv(1024).decode('utf-8')
alegere_client = int(alegere_client)
alegere_client = AlegeriJoc(alegere_client)
print(alegere_client) # Din 1, 2, 3
# server-ul isi alege cu ce joaca prin random
alegere_server = random.choice([AlegeriJoc.Piatra, AlegeriJoc.Hartie, AlegeriJoc.Foarfeca, AlegeriJoc.Soparla, AlegeriJoc.Spock])


mesaj_rezultat = ""
# daca alegerea server-ului si a noastra sunt la fel, egalitate
if alegere_client == alegere_server:
    mesaj_rezultat = "Egalitate"
# daca se gaseste alegerea random a server-ului in dictionar, castigam, altfel pierdem
elif alegere_server in logica_de_business[alegere_client]:
    mesaj_rezultat = "Ai castigat"
else:
    mesaj_rezultat = "Ai pierdut"

mesaj_rezultat += f', serverul a ales {alegere_server.name}, iar tu ai ales {alegere_client.name}'

# trimite server-ului client rezultatul
conn.send(bytes(mesaj_rezultat, 'utf-8'))