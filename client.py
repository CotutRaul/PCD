import os
import socket
import uuid

BUFFER_SIZE = 100000
SIZE = 1024

server_ip = '192.168.221.173'
port = 5566
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (server_ip, port)

try:
    client_socket.connect(server_address)
    print(f"Connected to server {server_ip}:{port}")
except ConnectionRefusedError:
    print(f"Failed to connect to server {server_ip}:{port}")
    exit(1)

while True:
    data_size = 0
    data = []

    print("1. Send data from file")
    print("2. 'q' to quit: ")

    message = input()

    if message == "q":
        break
    elif message == "1":
        current_dir = os.getcwd()
        file_list = os.listdir(current_dir)
        for path in file_list:
            if os.path.isfile(os.path.join(current_dir, path)):
                data.append(path)
                data_size += 1

        for i, path in enumerate(data):
            print(f"{i}. {path}")

        print("\nSelect the file you want to send!")
        message = input()

    # client_socket.sendall(data[int(message)].encode())

    filename = data[int(message)]
    print(filename)
    file_path = os.path.join(".", filename)

    with open(file_path, "r") as fp:
        lines = fp.readlines()
        for line in lines:
            line = line.strip()
            client_socket.sendall(line.encode())
            buffer = client_socket.recv(SIZE).decode('utf-8').replace('\0', '')
            # buffer = buffer[:-1]

            # print(buffer)
    client_socket.sendall(b"end")
    random_filename = str(uuid.uuid4())[:8] + ".txt"
    file = open(random_filename, "w")
    status = client_socket.recv(BUFFER_SIZE - 1).decode('utf-8').replace('\0', '')
    print(status + '\n')

    while coord := client_socket.recv(BUFFER_SIZE - 1).decode().replace('\0', ''):
        # buffer=buffer[:-1]
        print(coord)
        if coord == "end":
            break
        client_socket.sendall(b"got")

        file.write(coord + "\n")

        file.flush()
    os.fsync(file.fileno())
    file.close()
    client_socket.sendall(b"end")
    buffer = client_socket.recv(BUFFER_SIZE - 1).decode('utf-8').replace('\0', '')
    # buffer = client_socket.recv(BUFFER_SIZE - 1).decode('utf-8').replace('\0', '')


    response = client_socket.recv(BUFFER_SIZE - 1).decode('utf-8').replace('\0', '')
    print("\nServer response:", response)
    print("\nServer response: Check the folder out and the file:", random_filename)

client_socket.close()