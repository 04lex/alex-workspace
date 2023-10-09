import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 8007))

print('Connected')

while 1:
    message, address = server.recvfrom(1024)
    # message, address = server.recvfrom(65535).decode('utf-8')

    time.sleep(1)
    time_recv_message = time.time()
    print('Client:', message.decode('utf-8'))
    server.sendto(bytes(f'{time_recv_message}', encoding='utf-8'), address)
    server.sendto(bytes(f'Server: Message received', encoding='utf-8'),address)