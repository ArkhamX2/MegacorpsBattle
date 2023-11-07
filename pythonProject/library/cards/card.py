from enum import Enum
from library.player import Player
import pygame

RESOURSES_PATH = "pythonProject\\resourses\\"

class CardType(Enum):
    defence = 1
    attack = 2
    developer = 3
    event = 4


class Card(pygame.sprite.Sprite):


    def __init__(self, isOposite:bool, image:str):   
        self.cardImage = image     
        self.cardImageOposite = "cardOposite.png"
        self.isOposite = isOposite
        self.owner = 0
        self.isThrown = False
        self.isPlayed=False

        pygame.sprite.Sprite.__init__(self)
        
        if self.isOposite:
            self.image = pygame.image.load(RESOURSES_PATH + "cardOposite.png").convert_alpha() 
        else:
            self.image = pygame.image.load(RESOURSES_PATH + self.cardImage).convert_alpha()

        self.rect = self.image.get_rect(center=(0,0))

    def flip(self):
        self.isOposite = not(self.isOposite)
        
        if self.isOposite == True:
            self.image = pygame.image.load(RESOURSES_PATH + "cardOposite.png").convert_alpha() 
        elif self.isOposite == False:
            self.image = pygame.image.load(RESOURSES_PATH + self.cardImage).convert_alpha()


    def Throw(self):
        self.isThrown = True

    def __str__(self):
        string = "Card" + self.cardImage
        return string
    
