import socket
import random
import enum

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Reuse addr
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(('192.168.1.17', 8005))
server.listen()