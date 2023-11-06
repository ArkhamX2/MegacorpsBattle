from enum import Enum
import pygame

class CardType(Enum):
    defence = 1
    attack = 2
    developer = 3


class Card(pygame.sprite.Sprite):
    cardName:str
    cardDescription:str
    price:int
    

    def __init__(self,cardName:str, cardDescription:str, pos):        
        pygame.sprite.Sprite.__init__(self)
        # Загружаем спрайт игрока
        self.image = pygame.image.load("resourses\\card.png").convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.cardName = cardName
        self.cardDescription = cardDescription



    
