from library.cards.card import Card,CardType

class EventCard(Card):
    cardType = CardType.attack


    def __init__(self,isOposite:bool, image:str):
        super().__init__(isOposite,image)
