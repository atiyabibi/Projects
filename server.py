import socket
import os

# Server Setup
server_ip = '0.0.0.0'
server_port = 5001
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)

print(f"[*] Listening as {server_ip}:{server_port}")

# Accept client connection
client_socket, client_address = server_socket.accept()
print(f"[+] {client_address} connected.")

# Receive the file name
file_name = client_socket.recv(1024).decode()
print(f"Receiving the file: {file_name}")

# Create the file to store the received data
with open(f"received_{file_name}", 'wb') as file:
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        file.write(data)

print(f"[+] {file_name} received successfully.")

# Close the connection
client_socket.close()
server_socket.close()
