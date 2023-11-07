from library.cards.attackCard import *
from library.cards.defenceCard import *


class TransferCard:
    def __init__(self,intCard,isThrown,owner,isPlayed):
        self.intCard=intCard
        self.isThrown=isThrown
        self.owner=owner
        self.isPlayed=isPlayed

    def ReturnToCard(self):
        match self.intCard:
            case 0:
                Card=Advertisement(),
                Card[0].owner=self.owner
                Card[0].isThrown=self.isThrown
                Card[0].isPlayed=self.isPlayed
                return Card[0]
            case 1:
                Card=AntivirusSpyWorm(),
                Card[0].owner = self.owner
                Card[0].isThrown = self.isThrown
                Card[0].isPlayed = self.isPlayed
                return Card[0]
            case 2:
                Card=AntivirusTrojanBotnet(),
                Card[0].owner = self.owner
                Card[0].isThrown = self.isThrown
                Card[0].isPlayed = self.isPlayed
                return Card[0]
            case 3:
                Card=AntivirusTrojanWorm(),
                Card[0].owner = self.owner
                Card[0].isThrown = self.isThrown
                Card[0].isPlayed = self.isPlayed
                return Card[0]
            case 4:
                Card=BlockFishingScripting(),
                Card[0].owner = self.owner
                Card[0].isThrown = self.isThrown
                Card[0].isPlayed = self.isPlayed
                return Card[0]
            case 5:
                Card=DoSAttackCard(),
                Card[0].owner = self.owner
                Card[0].isThrown = self.isThrown
                Card[0].isPlayed = self.isPlayed
                return Card[0]
            case 6:
                Card=DoSDefence(),
                Card[0].owner = self.owner
                Card[0].isThrown = self.isThrown
                Card[0].isPlayed = self.isPlayed
                return Card[0]
            case 7:
                Card=TrojanCard(),
                Card[0].owner = self.owner
                Card[0].isThrown = self.isThrown
                Card[0].isPlayed = self.isPlayed
                return Card[0]
            case 8:
                Card=SpyCard(),
                Card[0].owner = self.owner
                Card[0].isThrown = self.isThrown
                Card[0].isPlayed = self.isPlayed
                return Card[0]



