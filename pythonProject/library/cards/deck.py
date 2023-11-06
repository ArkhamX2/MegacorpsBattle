import random
from library.cards.card import Card
from library.player import Player

MAX_DECK_SIZE = 30

class Deck:

    def __init__(self, cardList:[Card]):
        self.cardList = cardList
        tmp = []
        for i in range(MAX_DECK_SIZE):
            tmp.append(self.cardList[i%len(cardList)])
        random.shuffle(tmp)
        self.cards=tmp

    def deal(self, players:[Player]):
        for i in range(1,len(players)):
            cardCounter = self.checkIfFull(i)
            print(cardCounter)
            for card in self.cards:
                print("before dealed "+ str(card.owner)+ str(cardCounter))
                if card.owner == 0 and not(card.isThrown):
                    card.owner = i
                    cardCounter += 1
                    
                    print("dealed "+ str(card.owner)+ str(cardCounter))
                if cardCounter == 6:
                    break
                print("after dealed "+ str(card.owner)+ str(cardCounter))

            
                

    def checkIfFull(self,ownerId:int):
        counter = 0
        for card in self.cards:
            if card.owner == ownerId:
                counter += 1
        return counter

    def __str__(self):
        string = ""
        for card in self.cards:
            if card.owner == 1:
                string += str(card)
        string += "\nPlayer1:\n"
        for card in self.cards:
            if card.owner == 2:
                string += str(card)
        string += "\nPlayer2:\n"
        for card in self.cards:
            if card.owner == 3:
                string+=str(card)
        string += "\nPlayer3:\n"
        for card in self.cards:
            if card.owner == 4:
                string+=str(card)
        string += "\nPlayer4:\n"
        return string




    

