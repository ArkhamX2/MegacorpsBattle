import pygame
import sys
import random
from library.cards.card import Card
from library.cards.attackCard import *
from library.cards.defenceCard import *
from library.cards.developerCard import *
from library.player import Player
from UI.handBox import HandBox
from UI.handHandler import HandHandler
from UI.activeBox import ActiveBox
from UI.activeHandler import ActiveHandler

PURPLE = (162, 148, 210)
WHITE = (255, 255, 255)

def updateBackground():
    sc.fill(PURPLE)
    sf = pygame.image.load('pythonProject\\resourses\\Background.png')
    winSize = pygame.display.get_window_size()
    rt = sf.get_rect(center = (winSize[0]//2,winSize[1]//2))
    sc.blit(sf,rt)

pygame.init()
sc = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#sc = pygame.display.set_mode((Width, Height))
updateBackground()

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

handHandler = HandHandler(HandBox(1,deck))
activeHandler = ActiveHandler(ActiveBox(1,deck,False))

initialized = False
while 1:

    for i in pygame.event.get():
        keys = pygame.key.get_pressed()
        if i.type == pygame.QUIT:
            sys.exit()
        if keys[pygame.K_ESCAPE]:
            sys.exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                for i in range(0,6):
                    if (colliders[i]):
                        print(i)

    if initialized == False:
        handHandler.placeHand(sc)
        activeHandler.placeHand(sc)
        initialized = True
        updateBackground()

    point = pygame.mouse.get_pos()

    for i in range(0,6):
        colliders[i]=handHandler.handbox.rects[i].collidepoint(point)

    handHandler.update(sc)
    activeHandler.update(sc)

    pygame.display.update()

    pygame.time.delay(1)

    