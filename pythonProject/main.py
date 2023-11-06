from library.player import Player
from library.cards.attackCard import AttackCard
from library.cards.defenceCard import DefenceCard
from library.cards.developerCard import DeveloperCard

developer_cards = [DeveloperCard("Polina","UI"),DeveloperCard("Murad", "Server"),DeveloperCard("Vadim","Bugs")]
attack_cards = [AttackCard("Polina","UI"),AttackCard("Murad", "Server"),AttackCard("Vadim","Bugs")]
defence_cards = [DefenceCard("Polina","UI"),DefenceCard("Murad", "Server"),DefenceCard("Vadim","Bugs")]

player1 = Player("Timofey",0,attack_cards,defence_cards,developer_cards)
print(player1)