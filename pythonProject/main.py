import pygame
import sys
import random
from library.cards.card import Card
from library.cards.attackCard import *
from library.cards.defenceCard import *
from library.cards.developerCard import *
from library.player import Player

Width = 1366
Height = 768

GREEN = (200, 255, 200)
WHITE = (255, 255, 255)
pygame.init()
# sc = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
sc = pygame.display.set_mode((Width, Height))
sc.fill(GREEN)
sf = pygame.image.load('resourses\\Background.png')
rt = sf.get_rect(bottomright = (Width,Height))
sc.blit(sf,rt)

from library.cards.deck import Deck

players = [
    Player("Dealer",0),
    Player("Player1",1),
    Player("Player2",1),
    Player("Player3",1),
    Player("Player4",1),
]

deck = Deck(
        [Advertisement(),
        AntivirusSpyWorm(),
        AntivirusTrojanBotnet(),
        AntivirusTrojanWorm(),
        BlockFishingScripting(),
        DoSAttackCard(),
        DoSDefence(),
        TrojanCard(),
        SpyCard()
        ])




deck.deal(players)
for card in deck.cards:
    print(card.owner)

rects = []
for card in deck.cards:
    Card=card.ReturnToCard()
    rects.append(Card.rect)

while 1:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
 
    for i in range(0,len(deck.cards)):
        Card=deck.cards[i].ReturnToCard()
        sc.blit(Card.image, rects[i])
        pygame.display.update()
    
 
    pygame.time.delay(1000)

    