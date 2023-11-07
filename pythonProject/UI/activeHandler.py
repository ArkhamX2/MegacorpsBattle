import pygame

class ActiveHandler():

    def __init__(self,activeBox):
        self.activeBox = activeBox
    
    def update(self,source):
        self.activeBox.draw(source)
        
    def placeHand(self,source):
        winSize = pygame.display.get_window_size()
        self.activeBox.x,self.activeBox.y = winSize[0]//2 - (self.activeBox.hand[0].ReturnToCard(self.activeBox.hand[0].isOposite).rect.width+self.activeBox.hand[0].ReturnToCard(self.activeBox.hand[0].isOposite).rect.width//16)*1.5,winSize[1]//2 - 25
        self.activeBox.draw(source)