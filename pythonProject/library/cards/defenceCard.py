from library.cards.card import Card,CardType

class DefenceCard(Card):

    cardType = CardType.defence


    def __init__(self,isOposite:bool,image:str):
        super().__init__(isOposite,image)

class Advertisement(DefenceCard):
    
    def __init__(self, isOposite):
        super().__init__(isOposite,"Advertisement.png")
        
class AntivirusSpyWorm(DefenceCard):
    
    def __init__(self, isOposite):
        super().__init__(isOposite,"AntivirusSpyWorm.png")

class AntivirusTrojanBotnet(DefenceCard):
    
    def __init__(self, isOposite):
        super().__init__(isOposite,"AntivirusTrojanBotnet.png")

class AntivirusTrojanWorm(DefenceCard):
    
    def __init__(self, isOposite):
        super().__init__(isOposite,"AntivirusTrojanWorm.png")

class BlockFishingScripting(DefenceCard):
    
    def __init__(self, isOposite):
        super().__init__(isOposite,"BlockFishingScripting.png")

class DoSDefence(DefenceCard):
    
    def __init__(self, isOposite):
        super().__init__(isOposite,"DoSDefence.png")
        
class BrandmauerCard(DefenceCard):
    
    def __init__(self, isOposite):
        super().__init__(isOposite,"Branmauer.png")