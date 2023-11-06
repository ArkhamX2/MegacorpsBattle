from enum import Enum

class CardType(Enum):
    defence = 1
    attack = 2
    developer = 3


class Card:
    cardName:str
    cardDescription:str
    price:int
    

    def __init__(self,cardName:str, cardDescription:str):
        self.cardName = cardName
        self.cardDescription = cardDescription
    
