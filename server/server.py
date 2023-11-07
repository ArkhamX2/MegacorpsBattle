import socket
from _thread import *
import pickle

server = "localhost"
port = 6666

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

start_game=False
d={"PNum": [],"PHend": [[],[],[],[]], "BCards": [], "IsReady": [False, False, False, False]}

def threaded_client(conn, player):
    conn.send(pickle.dumps([d["PNum"][player],d["PHend"][player],d["BCards"],d["IsReady"]]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))

            d["PNum"][player] = data[0]
            d["PHend"][player] = data[1]
            d["BCards"] = data[2]
            d["IsReady"] = data[3]

            if not data:
                print("Disconnected")
                break
            else:
                reply=[d["PNum"][player],d["PHend"][player],d["BCards"],d["IsReady"]]

                #print("Received: ", data)
                #print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break
    print("Lost connection")
    conn.close()

currentPlayer = 0

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    d["PNum"].append(currentPlayer)
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
    if len(d["PNum"]) == 4:
        start_game=True