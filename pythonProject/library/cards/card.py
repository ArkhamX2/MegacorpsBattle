from enum import Enum
from library.player import Player
import pygame

RESOURSES_PATH = "pythonProject\\resourses\\"

class CardType(Enum):
    defence = 1
    attack = 2
    developer = 3


class Card(pygame.sprite.Sprite):
    isOposite:bool
    cardImage:str
    cardImageOposite:str
    owner:Player
    isThrown:bool
    

    def __init__(self, isOposite:bool, image:str):   
        self.cardImage = image     
        self.cardImageOposite = "cardOposite.png"
        self.isOposite = isOposite

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(RESOURSES_PATH + self.cardImage).convert_alpha()

        self.rect = self.image.get_rect(center=(0,0))
        self.flip()

    def flip(self):
        self.image = pygame.image.load(RESOURSES_PATH + self.cardImageOposite).convert_alpha() if self.isOposite else pygame.image.load(RESOURSES_PATH + self.cardImage).convert_alpha()
        
        if self.isOposite:
            self.image = pygame.image.load(RESOURSES_PATH + "cardOposite.png").convert_alpha() 
        else:
            self.image = pygame.image.load(RESOURSES_PATH + self.cardImage).convert_alpha()
        self.isOposite = not(self.isOposite)

    def Throw(self):
        self.isThrown = True

    
