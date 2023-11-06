import socket
from _thread import *
from player import Player
import pickle
import psutil

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


players = [Player(0,0,50,50,(255,0,0)), Player(100,100, 50,50, (0,0,255))]

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
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                #print("Received: ", data)
                #print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break
    user.connected=False
    print("Lost connection")
    conn.close()

def get_ip_addresses(family):
    for interface, snics in psutil.net_if_addrs().items():
        for snic in snics:
            if snic.family == -1 :
                mac = snic.address
            if snic.family == 2 :
                yield (interface, snic.address, snic.netmask, mac)

currentPlayer = 0
dt = list()
listusers=[]
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    ipv4 = list(get_ip_addresses(s))
    print(ipv4)
    if addr[0] in dt:
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