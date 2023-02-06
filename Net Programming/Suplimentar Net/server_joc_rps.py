import socket
import random
import enum

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Reuse addr
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(('127.0.0.1', 8104))
server.listen()

conn, address = server.accept()

choices = {"1": "Rock", "2": "Paper", "3": "Scissors"}
choose_msg = 'Pick one of: 1 - Rock, 2 - Paper, 3 - Scissors'

conn.send(bytes(choose_msg, 'utf-8'))

client_choice = conn.recv(1024).decode('utf-8')
print(client_choice)

server_choice = random.choice(["1", "2", "3"])

result_msg = ''

if client_choice == server_choice:
    result_msg = "Draw"
elif client_choice == "1":
    if server_choice == "2":
        result_msg = "You have been folded, you lost."
    else:
        result_msg = "You folded the computer, you won."
elif client_choice == "2":
    if server_choice == "3":
        result_msg = "You have been cut, you lost."
    else:
        result_msg = "You cut the computer, you won."
elif client_choice == "3":
    if server_choice == "1":
        result_msg = "You have been crushed, you lost."
    else:
        result_msg = "You crushed the computer, you won."

result_msg += f' You chose {client_choice}, the computer chose {server_choice}.'

conn.send(bytes(result_msg, 'utf-8'))