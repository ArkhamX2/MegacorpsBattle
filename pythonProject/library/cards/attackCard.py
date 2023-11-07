from library.cards.card import Card,CardType
from enum import Enum

class AttackCard(Card):

    cardType = CardType.attack


    def __init__(self,isOposite:bool, image:str):
        super().__init__(isOposite,image)

class TrojanCard(AttackCard):
    
    def __init__(self, isOposite):
        super().__init__(isOposite,"TrojanCard.png")

class SpyCard(AttackCard):

    def __init__(self, isOposite):
        super().__init__(isOposite,"SpyCard.png")

class FishingCard(AttackCard):

    def __init__(self, isOposite):
        super().__init__(isOposite,"FishingCard.png")

class DoSAttackCard(AttackCard):

    def __init__(self, isOposite):
        super().__init__(isOposite,"DoSAttackCard.png")

class BruteForceCard(AttackCard):

    def __init__(self, isOposite):
        super().__init__(isOposite, "BruteForce.png")


class SiteScriptingCard(AttackCard):

    def __init__(self, isOposite):
        super().__init__(isOposite,"SiteScripting.png")

        
class WormCard(AttackCard):

    def __init__(self, isOposite):
        super().__init__(isOposite,"Worm.png")
