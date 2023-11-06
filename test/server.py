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


players = [Player(0,0,50,50,(255,0,0)), Player(100,100, 50,50, (0,0,255)), Player(100,0,50,50,(0,255,0)), Player(0,100,50,50,(100,100,100))]

def threaded_client(conn, player, user):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                user.connected=False
                print("Disconnected")
                break
            else:
                reply=[currentPlayer]
                for i in range(len(players)):
                    if (i!=player):
                        reply.append(players[i])

                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break
    user.connected=False
    print("Lost connection")
    conn.close()

currentPlayer = 0
dt = list()
listusers=[]
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    if addr[0] in dt and False:
        for user in listusers:
            if user.connected != True and addr[0]==user.ip:
                user.connected=True
                start_new_thread(threaded_client, (conn, user.id,user))

    else:
        dt.append(addr[0])
        print(dt)
        listusers.append(User(currentPlayer, addr[0]))
        start_new_thread(threaded_client, (conn, currentPlayer,listusers[len(listusers)-1]))
        currentPlayer += 1