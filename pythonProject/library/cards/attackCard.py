from library.cards.card import Card,CardType
from enum import Enum

class AttackCard(Card):

    cardType = CardType.attack


    def __init__(self,isOposite:bool, image:str):
        super().__init__(isOposite,image)

class TrojanCard(AttackCard):
    
    def __init__(self):
        super().__init__(True,"TrojanCard.png")

class SpyCard(AttackCard):

    def __init__(self):
        super().__init__(True,"SpyCard.png")

class FishingCard(AttackCard):

    def __init__(self):
        super().__init__(True,"FishingCard.png")

class DoSAttackCard(AttackCard):

    def __init__(self):
        super().__init__(True,"DoSAttackCard.png")
