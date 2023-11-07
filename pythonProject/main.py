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

PURPLE = (162, 148, 210)
WHITE = (255, 255, 255)
pygame.init()
# sc = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
sc = pygame.display.set_mode((Width, Height))
sc.fill(PURPLE)
sf = pygame.image.load('pythonProject\\resourses\\Background.png')
rt = sf.get_rect(center = (Width//2,Height//2))
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
        [Advertisement(True),
        AntivirusSpyWorm(True),
        AntivirusTrojanBotnet(True),
        AntivirusTrojanWorm(True),
        BlockFishingScripting(True),
        DoSAttackCard(True),
        DoSDefence(True),
        TrojanCard(True),
        SpyCard(True),
        BruteForceCard(True),
        SiteScriptingCard(True),
        WormCard(True),
        BrandmauerCard(True),
        PetrDeveloper(True),
        MatveyDeveloper(True),
        AlekseyDeveloper(True),
        Tester137Developer(True),
        Tester139Developer(True),
        Tester137GoldDeveloper(True)
        ])

deck.deal(players)

hand = HandBox(1,deck)

while 1:

    for i in pygame.event.get():
        keys = pygame.key.get_pressed()
        if i.type == pygame.QUIT:
            sys.exit()
        if keys[pygame.K_ESCAPE]:
            sys.exit()

    hand.draw(sc)
    hand.flip()
    pygame.display.update()

    pygame.time.delay(100)

    