from library.cards.card import Card, CardType

class DeveloperCard(Card):

    cardType = CardType.developer

    def __init__(self,name:str,description:str):
        super().__init__(name,description)


class PetrDeveloper(DeveloperCard):
    
    def __init__(self, isOposite):
        super().__init__(isOposite,"PetrDev.png")

class MatveyDeveloper(DeveloperCard):
    
    def __init__(self, isOposite):
        super().__init__(isOposite,"MatveyDev.png")
        
class Tester139Developer(DeveloperCard):
    
    def __init__(self, isOposite):
        super().__init__(isOposite,"Tester139.png")

class Tester137Developer(DeveloperCard):
    
    def __init__(self, isOposite):
        super().__init__(isOposite,"Tester137.png")

class Tester137GoldDeveloper(DeveloperCard):
    
    def __init__(self, isOposite):
        super().__init__(isOposite,"Tester137Gold.png")
        
class AlekseyDeveloper(DeveloperCard):
    
    def __init__(self, isOposite):
        super().__init__(isOposite,"AlekseyDev.png")
