from library.cards.card import Card,CardType

class DefenceCard(Card):

    cardType = CardType.defence


    def __init__(self,isOposite:bool,image:str):
        super().__init__(isOposite,image)

class Advertisement(DefenceCard):
    
    def __init__(self):
        super().__init__(True,"Advertisement.png")
        
class AntivirusSpyWorm(DefenceCard):
    
    def __init__(self):
        super().__init__(True,"AntivirusSpyWorm.png")

class AntivirusTrojanBotnet(DefenceCard):
    
    def __init__(self):
        super().__init__(True,"AntivirusTrojanBotnet.png")

class AntivirusTrojanWorm(DefenceCard):
    
    def __init__(self):
        super().__init__(True,"AntivirusTrojanWorm.png")

class BlockFishingScripting(DefenceCard):
    
    def __init__(self):
        super().__init__(True,"BlockFishingScripting.png")

class DoSDefence(DefenceCard):
    
    def __init__(self):
        super().__init__(True,"DoSDefence.png")