import pygame
import sys
import random
from library.cards.card import Card
from library.cards.attackCard import *
from library.cards.defenceCard import *
from library.cards.developerCard import *
from library.player import Player
from UI.handBox import HandBox

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
    Player(0,"Dealer",0),
    Player(1,"Player1",1),
    Player(2,"Player2",1),
    Player(3,"Player3",1),
    Player(4,"Player4",1),
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

<<<<<<< Updated upstream
rects = []
for card in deck.cards:
    Card=card.ReturnToCard()
    rects.append(Card.rect)
=======
hand = HandBox(1,deck)
>>>>>>> Stashed changes

while 1:

    for i in pygame.event.get():
        keys = pygame.key.get_pressed()
        if i.type == pygame.QUIT:
            sys.exit()
<<<<<<< Updated upstream
 
    for i in range(0,len(deck.cards)):
        Card=deck.cards[i].ReturnToCard()
        sc.blit(Card.image, rects[i])
        pygame.display.update()
    
 
    pygame.time.delay(1000)
=======
        if keys[pygame.K_ESCAPE]:
            sys.exit()

    hand.draw(sc)
    pygame.display.update()

    pygame.time.delay(20)
>>>>>>> Stashed changes

    