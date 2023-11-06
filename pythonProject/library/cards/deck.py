import random
from library.cards.card import Card

MAX_DECK_SIZE = 112

class Deck:

    def __init__(self, cardList:[Card]):
        self.cardList = cardList
        tmp = []
        for i in range(MAX_DECK_SIZE):
            tmp.append(self.cardList[i%len(cardList)])
        print(tmp)
        random.shuffle(tmp)
        self.cards=tmp

    

