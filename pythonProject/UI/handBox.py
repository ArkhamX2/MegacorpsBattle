from library.cards.deck import Deck
from library.cards.card import Card
import pygame

class HandBox(): 
    def __init__(self, ownerID:int, deck:Deck, x:int = 0, y:int = 0):
        self.rects = []
        self.hand = []
        self.x = x
        self.y = y
        for card in deck.cards:
            if card.owner == ownerID:
                self.hand.append(card)
                self.rects.append(card.ReturnToCard().rect)
    
    def place(self):
        for i in range(0,len(self.rects)):
            self.rects[i].x,self.rects[i].y = self.x+10,self.y+10
            self.rects[i].x += self.rects[i].width *i
            self.rects[i].y += self.rects[i].height*i
            self.hand[i].ReturnToCard().flip()
            pygame.display.update()
        

    def draw(self,source):
        self.place()
        for i in range(0,len(self.hand)):
            source.blit(self.hand[i].ReturnToCard().image, self.rects[i])
            pygame.display.update()
        