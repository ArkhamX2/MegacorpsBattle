from library.cards.card import Card, CardType

class DeveloperCard(Card):

    cardType = CardType.developer

    def __init__(self,name:str,description:str):
        super().__init__(name,description)
