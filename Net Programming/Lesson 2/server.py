# sectiunea importuri
import socket
import random

# socket.AF_INET = Familia de adrese IP -> versiunea 4
# socket.SOCK_STREAM = Tipul de socket creat (TCP)
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# bind -> legat la adresa di port
serverSocket.bind(("127.0.0.1" ,8006))

# listen -> ascultat de portul respectiv
serverSocket.listen()


# De trimis -> clientSocket.send

# De primit -> clientSocket.recv
conexiune, adresa = serverSocket.accept()

data = conexiune.recv(1024)
nr_primit = data.decode("utf-8")
print("Serverul a primit: ", nr_primit)

# server
nr_server = random.randint(1, 5)

# Comparatie ce se primeste cu ce genereaza serverul
if nr_primit == nr_server:
    conexiune.send(bytes('Ati ghicit', 'utf-8'))
else:
    conexiune.send(bytes(f'Nu ati ghicit numarul, serverul a ales {nr_server}', 'utf-8'))