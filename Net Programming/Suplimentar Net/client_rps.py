import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.1.17', 8005))

first_message = client.recv(1024).decode('utf-8')
client_choice = input(first_message + "\n")

client.send(bytes(client_choice, 'utf-8'))

result = client.recv(1024).decode('utf-8')
print(result)