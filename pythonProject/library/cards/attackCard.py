from library.cards.card import Card,CardType

class AttackCard(Card):

    cardType = CardType.attack


    def __init__(self,name:str,description:str):
        super().__init__(name,description)
