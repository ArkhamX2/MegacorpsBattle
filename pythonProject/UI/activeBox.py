from library.cards.deck import Deck
import pygame

class ActiveBox():
    def __init__(self, ownerID:int, deck:Deck,isHorizontal:bool, x:int = 0, y:int = 0):
        self.rects = []
        self.hand = []
        self.isHorizontal = isHorizontal
        self.x = x
        self.y = y
        for card in deck.cards[1:4]:
            if card.owner == ownerID:
                self.hand.append(card)
                self.rects.append(card.ReturnToCard(card.isOposite).rect)
    
    def placeCards(self):
        if self.isHorizontal:
            for i in range(0,len(self.rects)):
                self.rects[i].x,self.rects[i].y = self.x+10,self.y+10
                self.rects[i].x += self.rects[i].width*i + i*(self.rects[i].width//16)
        else:
            for i in range(0,len(self.rects)):
                pygame.transform.rotate(self.hand[i].ReturnToCard(self.hand[i].isOposite).image, 180)
                self.rects[i].x,self.rects[i].y = self.x+10,self.y+10
                self.rects[i].y += self.rects[i].width*i + i*(self.rects[i].width//16)



        
    def flip(self):
        for i in range(0,len(self.rects)):
            self.hand[i].ReturnToCard(self.hand[i].isOposite).flip()
            self.hand[i].isOposite = not(self.hand[i].isOposite)
            pygame.display.update()


    def draw(self,source):
        self.placeCards()
        if self.hand[0].isOposite:
            self.flip()
        for i in range(0,len(self.hand)):
            source.blit(self.hand[i].ReturnToCard(self.hand[i].isOposite).image, self.rects[i])
            pygame.display.update()