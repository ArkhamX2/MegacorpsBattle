import socket
from _thread import *
from player import Player
import pickle

class User():
    def __init__(self, id, ip):
        self.id=id
        self.ip=ip
        self.connected=True

server = "localhost"
port = 6666

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

d={"PHend": [[],[],[],[]], "BCards": [], "IsReady": [False, False, False, False]}

def threaded_client(conn, player):
    conn.send(pickle.dumps([d["PHend"][player],d["BCards"],d["IsReady"]]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))

            d["PHend"][player] = data[0]
            d["BCards"]=data[1]
            d["IsReady"]=data[2]

            if not data:
                print("Disconnected")
                break
            else:
                reply=[d["PHend"][player],d["BCards"],d["IsReady"]]

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
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1