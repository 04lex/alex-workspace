import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

time_client_message = time.time()
client.sendto(bytes('Message from client', encoding='utf-8'), ('127.0.0.1', 8007))

# time_back, addr = client.recvfrom(65535).decode('utf-8')
time_back, addr = client.recvfrom(1024)
time_back = time_back.decode('utf-8')

print(f'Message sent in: {float(time_back) - time_client_message}')

message, addr = client.recvfrom(1024)
print(message.decode('utf-8'))