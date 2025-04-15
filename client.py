import socket
import os

# Client Setup
server_ip = '127.0.0.1'
server_port = 5001
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_ip, server_port))

# Specify the file to send (change the filename to your actual file)
file_name = 'testfile.txt'  # Make sure the file exists in the same directory as client.py

# Send the file name to the server
client_socket.send(file_name.encode())

# Open the file to send
with open(file_name, 'rb') as file:
    while True:
        # Read and send file in chunks of 1024 bytes
        file_data = file.read(1024)
        if not file_data:
            break
        client_socket.send(file_data)

print(f"[+] {file_name} sent successfully.")

# Close the connection
client_socket.close()
