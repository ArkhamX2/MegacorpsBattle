from library.user import User
from library.cards.defenceCard import DefenceCard
from library.cards.developerCard import DeveloperCard
from library.cards.attackCard import AttackCard


class Player(User):
    attack_cards:[AttackCard]
    defence_cards:[DefenceCard]
    developer_cards:[DeveloperCard]
    development_points:int
    name:str

    def __init__(self,name:str, developmentPoints:int, attack_cards: [AttackCard],defence_cards: [DefenceCard],developer_cards: [DeveloperCard]):
        super().__init__(0,name)
        self.attack_cards = attack_cards
        self.defence_cards = defence_cards
        self.developer_cards = developer_cards
        self.development_points = developmentPoints

    def __str__(self):
        string = f"{self.name} {self.development_points}"
        for card in self.attack_cards:
            string += card.cardName
        string += '\n'
        for card in self.defence_cards:
            string += card.cardName
        string += '\n'
        for card in self.developer_cards:
            string += card.cardName
        string += '\n'
        return string

