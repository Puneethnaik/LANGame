import socket
import threading

HEADER = 64

PORT = 5050

SERVER = socket.gethostbyname(socket.gethostname())  # Will automatically find local ip address

ADDR = (SERVER, PORT)

FORMAT = "utf-8"

DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = []

x = 700
y = 700


def handle_client(conn, addr):
    thingToReturn = ""
    connected = True
    print(f"[CONNECTION] {addr}")
    while connected:
        data = conn.recv(1024)
        if not data:
            break
        print(f"[CONNECTION] new connection from : {addr}, Command: {str(data)}")
        data = data.decode(FORMAT)
        if data == "getpos":
            thingToReturn = str(f"{x}, {y}")
        conn.send(thingToReturn.encode(FORMAT))
    conn.close()



def returnMessage():
    for client in clients:
        print(client)

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


print("[STARTING] server is starting...")
start()
