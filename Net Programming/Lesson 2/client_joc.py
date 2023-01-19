import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8007))

primul_mesaj_primit = client.recv(1024).decode('utf-8')
alegere = input(primul_mesaj_primit + '\n')

client.send(bytes(alegere, 'utf-8'))

mesaj_rezultat = client.recv(1024).decode('utf-8')
print(mesaj_rezultat)

