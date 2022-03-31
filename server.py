import pickle
import socket
import sys
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # defining ac TCP socket (IPv4 Internet protocol)
FORMAT = 'utf-8'
HOST_IP = 'localhost'
connected_clients = []
connected_nicknames = []


def broadcast(sender, message, action):
    for c in connected_clients:
        data = pickle.dumps((sender, message, action))
        c.send(data)


def handle(client):
    while True:
        try:
            sender, message = pickle.loads(client.recv(1024))
            broadcast(sender, message, None)
        except:
            index = connected_clients.index(client)
            connected_clients.remove(client)
            client.close()
            nickname = connected_nicknames[index]
            broadcast(client, f"{nickname} left the chat".encode(FORMAT), None)
            connected_nicknames.remove(nickname)
            break


def initiate_dialogue_round(action):
    suggestion_message = "Do you guys want to {}?".format(action)
    broadcast("SERVER", suggestion_message, action)


# Port assigned by command line parameter 2 or printing explanations of command line parameters:
try:
    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print("::::::::::::HELP MESSAGE::::::::::::\n"
              "To start the server you have to enter a desired port, like shown below:\n\n"
              "python server.py PORT\n\n"
              "::::::::::::::::::::::::::::::::::::::")
        sys.exit()
    PORT = int(sys.argv[1])
except(IndexError, ValueError):
    print("::::::::::::ERROR MESSAGE::::::::::::\n"
          "PORT needs to be specified. See example below with port 1234:\n\n"
          "python server.py 1234\n\n"
          "::::::::::::::::::::::::::::::::::::::")
    sys.exit()

server.bind((HOST_IP, PORT))
server.listen(4)  # allows the server to listen for connections

print("[STARTING] server is started and listening for connections...")

while True:
    client, address = server.accept()
    bot_name = client.recv(1024).decode(FORMAT)
    connected_nicknames.append(bot_name)
    connected_clients.append(client)

    print(f"{bot_name.upper()} with address ('{address[0]}', {address[1]}) has joined the chat.")
    client.send("Welcome to the bot-server!".encode(FORMAT))
    # broadcast("SERVER", f"{bot_name.upper} has joined the chat!", None)

    thread = threading.Thread(target=handle, args=(client,))
    thread.start()

    if len(connected_clients) > 3:
        initiate_dialogue_round("eat")  # Automatically initiating a round of dialogue when 4 bots are connected
