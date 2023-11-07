import pygame

class HandHandler():

    def __init__(self,handbox):
        self.handbox = handbox
    
    def update(self,source):
        self.handbox.draw(source)
        
    def placeHand(self,source):
        winSize = pygame.display.get_window_size()
        self.handbox.x,self.handbox.y = winSize[0]//2 - (self.handbox.hand[0].ReturnToCard(self.handbox.hand[0].isOposite).rect.width+self.handbox.hand[0].ReturnToCard(self.handbox.hand[0].isOposite).rect.width//16)*3,winSize[1]//2 +(self.handbox.hand[0].ReturnToCard(self.handbox.hand[0].isOposite).rect.height)//2 + 25
        self.handbox.draw(source)