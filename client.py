import pickle
import socket
import sys
import bots
import time
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # defining a TCP socket (IPv4 Internet protocol)
FORMAT = 'utf-8'
available_bots = {"mj", "lebron", "lavine", "kobe"}

try:
    IP = sys.argv[1]  # saves IP address from second argument
    if IP == '-h' or IP == '--help':
        print("::::::::::::HELP MESSAGE::::::::::::\n"
              "To connect the client to a server with a specified IP and PORT, write the following:\n\n"
              "python client.py IP PORT BOT_NAME\n\n"
              "Available bots: MJ, Lebron, Lavine, Kobe\n"
              "::::::::::::::::::::::::::::::::::::::"
              )
        sys.exit()

    PORT = int(sys.argv[2])
    bot_argument = sys.argv[3].lower()

    if bot_argument in available_bots:
        bot_name = bot_argument
    else:
        print(f"The bot {sys.argv[3]} is not available, but you can try one of these:\n"
              f"{list(available_bots)}")
        sys.exit()
except(IndexError, ValueError):
    print("::::::::::::ERROR MESSAGE::::::::::::\n"
          "IP, PORT and BOT need to be specified. Example:\n\n"
          "python client.py localhost 1234 Lebron\n\n"
          "Available bots: MJ, Lebron, Lavine, Kobe\n"
          "::::::::::::::::::::::::::::::::::::::")
    # EDIT ^
    sys.exit()

client.connect((IP, PORT))  # Client connecting to server with specified IP and PORT
client.send(bot_name.encode(FORMAT))  # Client sending a message to the server

server_msg = client.recv(1024)  # receiving message sent from server in utf-8 format
server_msg = server_msg.decode(FORMAT)  # decoding message to utf-8 format
print(server_msg)  # printing the server message in client's terminal


def receive_message():
    while True:
        try:
            sender, message, action = pickle.loads(client.recv(1024))
            print(f"{sender}: {message}")

            if sender == "SERVER":
                response = bots.bot_response(bot_name.lower(), action)
                data = pickle.dumps((bot_name, response))
                client.send(data)
        except(OSError, ConnectionAbortedError, EOFError):
            print("Could not establish connection with server")
            client.close()
            break
        time.sleep(.3)


threading.Thread(target=receive_message).start()
