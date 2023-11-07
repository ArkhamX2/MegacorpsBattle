from library.cards.attackCard import *
from library.cards.defenceCard import *


class TransferCard:
    def __init__(self,intCard,isThrown,owner,isOposite,isPlayed):
        self.intCard=intCard
        self.isThrown=isThrown
        self.owner=owner
        self.isPlayed=isPlayed
        self.isOposite = isOposite

    def ReturnToCard(self,isOposite):
        match self.intCard:
            case 0:
                Card=Advertisement(isOposite),
                Card[0].owner=self.owner
                Card[0].isThrown=self.isThrown
                Card[0].isPlayed=self.isPlayed
                Card[0].isOposite=isOposite
                return Card[0]
            case 1:
                Card=AntivirusSpyWorm(isOposite),
                Card[0].owner = self.owner
                Card[0].isThrown = self.isThrown
                Card[0].isPlayed = self.isPlayed
                Card[0].isOposite=isOposite
                return Card[0]
            case 2:
                Card=AntivirusTrojanBotnet(isOposite),
                Card[0].owner = self.owner
                Card[0].isThrown = self.isThrown
                Card[0].isPlayed = self.isPlayed
                Card[0].isOposite=isOposite
                return Card[0]
            case 3:
                Card=AntivirusTrojanWorm(isOposite),
                Card[0].owner = self.owner
                Card[0].isThrown = self.isThrown
                Card[0].isPlayed = self.isPlayed
                Card[0].isOposite=isOposite
                return Card[0]
            case 4:
                Card=BlockFishingScripting(isOposite),
                Card[0].owner = self.owner
                Card[0].isThrown = self.isThrown
                Card[0].isPlayed = self.isPlayed
                Card[0].isOposite=isOposite
                return Card[0]
            case 5:
                Card=DoSAttackCard(isOposite),
                Card[0].owner = self.owner
                Card[0].isThrown = self.isThrown
                Card[0].isPlayed = self.isPlayed
                Card[0].isOposite=isOposite
                return Card[0]
            case 6:
                Card=DoSDefence(isOposite),
                Card[0].owner = self.owner
                Card[0].isThrown = self.isThrown
                Card[0].isPlayed = self.isPlayed
                Card[0].isOposite=isOposite
                return Card[0]
            case 7:
                Card=TrojanCard(isOposite),
                Card[0].owner = self.owner
                Card[0].isThrown = self.isThrown
                Card[0].isPlayed = self.isPlayed
                Card[0].isOposite=isOposite
                return Card[0]
            case 8:
                Card=SpyCard(isOposite),
                Card[0].owner = self.owner
                Card[0].isThrown = self.isThrown
                Card[0].isPlayed = self.isPlayed
                Card[0].isOposite=isOposite
                return Card[0]



