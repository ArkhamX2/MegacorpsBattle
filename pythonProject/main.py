import pygame
import sys
import random
from library.cards.card import Card
from library.cards.attackCard import *
from library.cards.defenceCard import *
from library.cards.developerCard import *


GREEN = (200, 255, 200)
WHITE = (255, 255, 255)
pygame.init()
# sc = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
sc = pygame.display.set_mode((800, 700))
sc.fill(GREEN)

from library.cards.deck import Deck

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
        
rects = []
for card in deck.cards:
    rects.append(card.rect)

sc.fill(GREEN)

while 1:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
 
    for i in range(0,len(deck.cards)):
        sc.blit(deck.cards[i].image, rects[i])
        pygame.display.update()
    
 
    pygame.time.delay(1000)

    