import socket
import pygame
from _thread import *
import pickle
from library.cards.card import Card
from library.cards.attackCard import *
from library.cards.defenceCard import *
from library.cards.developerCard import *
from library.player import Player
from UI.handBox import HandBox
from library.cards.deck import Deck

server = "localhost"
port = 6666
Width = 100
Height = 100

GREEN = (200, 255, 200)
WHITE = (255, 255, 255)
pygame.init()
sc = pygame.display.set_mode((Width, Height))
sc.fill(GREEN)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

start_game=False
d={"PNum": [],"PHend": [[],[],[],[]], "BCards": [], "IsReady": [False, False, False, False]}
deck=Deck()
def startNewGame():
    print("Starting game...")
    players = [
        Player(d["PNum"][0], "Player1", 1),
        Player(d["PNum"][1], "Player2", 1),
        Player(d["PNum"][2], "Player3", 1),
        Player(d["PNum"][3], "Player4", 1),
        Player(0, "Dealer", 0),
    ]
    deck = Deck(
        [Advertisement(True),
         AntivirusSpyWorm(True),
         AntivirusTrojanBotnet(True),
         AntivirusTrojanWorm(True),
         BlockFishingScripting(True),
         DoSAttackCard(True),
         DoSDefence(True),
         TrojanCard(True),
         SpyCard(True)
         ])

    deck.deal(players)
    for player in players:
        if player.id!=0:
            d["PHend"][player.id-1]=deck.getCardById(player.id)
            print(len(d["PHend"][player.id-1]))
            d["BCards"]+=deck.getCardById(player.id)

def giveCart(players):
    deck.deal(players)
    for player in players:
        if player.id != 0:
            d["PHend"][player.id - 1] = deck.getCardById(player.id)
            print(len(d["PHend"][player.id - 1]))
            d["BCards"] += deck.getCardById(player.id)


#d={"PNum": [],"PHend": [[],[],[],[]], "BCards": [], "IsReady": [False, False, False, False]}
def threaded_client(conn, player):
    player-=1
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

currentPlayer = 1

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    d["PNum"].append(currentPlayer)
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
    if len(d["PNum"]) == 4:
        start_game=True
        startNewGame()