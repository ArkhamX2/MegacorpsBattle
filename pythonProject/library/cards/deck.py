import copy
import random
from library.cards.card import Card
from library.player import Player

from library.cards.TransferCard import TransferCard

MAX_DECK_SIZE = 4

class Deck:

    def __init__(self, cardList:[Card]):
        self.cardList = cardList
        tmp = []
        for i in range(MAX_DECK_SIZE*len(cardList)):
            tmp.append( TransferCard(i%len(cardList),0,0,0))
        #random.shuffle(tmp)
        self.cards=tmp

    def shufle(self):
        random.shuffle(self.cards)
        return


    def deal(self, players:[Player]):
        for i in range(1,len(players)):
            cardCounter = self.checkIfFull(i)
 
            for card in self.cards:
                if card.owner == 0 and not(card.isThrown):
                    card.owner = i
                    cardCounter += 1
                    
                if cardCounter == 6:
                    break

            
                

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
    def getCardById(self,id:int):
        list=[]
        for card in self.cards:
            if card.owner==id:
                list.append(copy.deepcopy(card))
        return list
    def getThrownCard(self):
        list = []
        for card in self.cards:
            if card.isThrown == True:
                list.append(copy.deepcopy(card))
        return list
    def getIsPlayedCard(self):
        list = []
        for card in self.cards:
            if card.isPlayed == True:
                list.append(copy.deepcopy(card))
        return list
    def getIsUnPlayedCard(self):
        list = []
        for card in self.cards:
            if card.isPlayed == False:
                list.append(copy.deepcopy(card))
        return list
    def getThrownCard(self):
        list = []
        for card in self.cards:
            if card.isThrown == False:
                list.append(copy.deepcopy(card))
        return list





    

