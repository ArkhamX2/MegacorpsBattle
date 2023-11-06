from library.cards.card import Card,CardType

class DefenceCard(Card):

    cardType = CardType.defence


    def __init__(self,name:str,description:str):
        super().__init__(name,description)


