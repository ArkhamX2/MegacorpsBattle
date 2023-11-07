from library.cards.deck import Deck
from library.cards.card import Card
import pygame

class HandBox(): 
    def __init__(self, ownerID:int, deck:Deck, x:int = 0, y:int = 0):
        self.rects = []
        self.hand = []
        for card in deck.cards:
            if card.owner == ownerID:
                self.hand.append(card)
                self.rects.append(card.ReturnToCard().rect)
    
    def draw(self,source):
        for i in range(0,len(self.hand)):
            self.rects[i].x,self.rects[i].y = 0,0
            self.rects[i].x += self.rects[i].width+i+10
            source.blit(self.hand[i].ReturnToCard().image, self.rects[i])
            pygame.display.update()
        