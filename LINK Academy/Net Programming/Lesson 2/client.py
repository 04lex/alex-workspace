import socket

# client
nr_client = input("Introduceti un numar intre 1 si 5: \n")


# socket.AF_INET = Familia de adrese IP -> versiunea 4
# socket.SOCK_STREAM = Tipul de socket creat (TCP)
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Creez conexiunea de tip socket
clientSocket.connect(("127.0.0.1", 8006))

# De trimis -> clientSocket.send
clientSocket.send(bytes(nr_client, "utf-8"))

mesajul_primit = clientSocket.recv(1024).decode("utf-8")
print(mesajul_primit)

# De primit -> clientSocket.recv
