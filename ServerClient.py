import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9090
SERVER_ADDR = (HOST, PORT)
DISCONNECT_MSG = "DEAD"
FORMAT = 'utf-8'

print("Do you want a server or client?")
print("Enter S or C.")

answer = input('--> ').upper()

# Server socket
if answer == "S":
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    server_socket.bind(SERVER_ADDR)


    def handle_a_client(connection, address):
        print(f'Connection from: {address}')

        connected_1 = True
        while connected_1:
            data_from_client = connection.recv(4096).decode(FORMAT)
            print(f'From {address}: ' + str(data_from_client))

            if data_from_client != DISCONNECT_MSG:
                data_to_client = input('--> ')
                connection.send(data_to_client.encode(FORMAT))

            else:
                connected_1 = False

        connection.close()
        print(f'{address} has DISCONNECTED')

    # starting
    def start():
        print("-------------------------------------------")
        print("[ESTABLISHING]")
        print(f"Server is established on {SERVER_ADDR}")
        server_socket.listen()

        while True:
            connection, address = server_socket.accept()
            # json data from client which has (user, private_key)
            thread = threading.Thread(target=handle_a_client, args=(connection, address))
            thread.start()
            print(f'CONNECTIONS: {threading.active_count() - 1}')


    print("[BEGIN]")
    print("Server has started.......")
    start()

# Client Socket
if answer == "C":
    client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    client_socket.connect(SERVER_ADDR)

    print("Waiting for connection....")

    def send_to_server_and_recv(data_to_server):
        data_to_server = message.encode(FORMAT)
        client_socket.send(data_to_server)

        data_from_server = client_socket.recv(1024).decode(FORMAT)
        print(f'Server: {data_from_server}')


    print("[CONNECTED]")
    print(f"Your Server is: {SERVER_ADDR}")

    connected = True
    while connected:
        message = input('--> ')
        send_to_server_and_recv(message)

        if message == DISCONNECT_MSG:
            connected = False

    client_socket.close()
    print("[DISCONNECTED]")
