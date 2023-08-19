import socket
import threading

# Defining variables which are going to be repeatedly used
HOST = socket.gethostbyname(socket.gethostname())
PORT = 9090
SERVER_ADDR = (HOST, PORT)
DISCONNECT_MSG = "DEAD"
FORMAT = 'utf-8'

# Making a choice to discard the usage of two separate code for server and client
print("Do you want a server or client?")
print("Enter S or C.")

answer = input('--> ').upper()

# Server socket
if answer == "S":
    
    # Initialising and defining a server socket
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    server_socket.bind(SERVER_ADDR)


    def handle_a_client(connection, address):
        print(f'Connection from: {address}')

        connected_1 = True
        while connected_1:
            data_from_client = connection.recv(4096).decode(FORMAT)
            print(f'From {address}: ' + str(data_from_client))

            # If the received message is not disconnect message then continue to send data
            if data_from_client != DISCONNECT_MSG:
                data_to_client = input('--> ')
                connection.send(data_to_client.encode(FORMAT))

            # change connected_1 flag to false and exit the loop
            else:
                connected_1 = False

        connection.close()
        print(f'{address} has DISCONNECTED')

    # starting the server socket
    def start():
        print("-------------------------------------------")
        print("[ESTABLISHING]")
        print(f"Server is established on {SERVER_ADDR}")
        server_socket.listen()

        while True:
            connection, address = server_socket.accept()
            thread = threading.Thread(target=handle_a_client, args=(connection, address))
            thread.start()
            print(f'CONNECTIONS: {threading.active_count() - 1}')


    print("[BEGIN]")
    print("Server has started.......")
    start()

# Client Socket
if answer == "C":
    # Initialising and defining the type of client socket
    client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    client_socket.connect(SERVER_ADDR)

    print("Waiting for connection....")

    # function which sends and receive data to and from server
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
