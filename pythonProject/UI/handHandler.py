import pygame

class HandHandler():

    def __init__(self,handbox):
        self.handbox = handbox
    
    def update(self,source):
        self.handbox.draw(source)
        
    def placeHand(self,source):
        winSize = pygame.display.get_window_size()
        self.hand.x,self.hand.y = winSize[0]//2 - (self.hand.hand[0].ReturnToCard(self.hand.hand[0].isOposite).rect.width+self.hand.hand[0].ReturnToCard(self.hand.hand[0].isOposite).rect.width//16)*3,winSize[1]//2 +(self.hand.hand[0].ReturnToCard(self.hand.hand[0].isOposite).rect.height)//2+30
        self.hand.draw(source)
