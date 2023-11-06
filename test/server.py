import socket
from _thread import *
import sys

class User():
    def __init__(self, id, ip):
        self.id=id
        self.ip=ip
        self.connected=True

#server = "10.160.2.103"
server = "localhost"
port = 6666

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

pos = [(0,0),(100,100)]

def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                #print("Received: ", data)
                #print("Sending : ", reply)

            conn.sendall(str.encode(make_pos(reply)))
        except:
            break

    print("Lost connection")
    conn.close()
dt = list()
listusers=[]
currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    if addr[0] in dt:
        print('ASdasdasdasd')
        for user in listusers:
            if user.connected != True:
                start_new_thread(threaded_client, (user.ip, user.id))
    else:
        dt.append(addr[0])
        print(dt)
        listusers.append(User(currentPlayer, addr[0]))
        start_new_thread(threaded_client, (conn, currentPlayer))
        currentPlayer += 1