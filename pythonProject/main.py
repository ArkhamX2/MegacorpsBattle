import pygame
import sys
from library.cards.card import Card
 
GREEN = (200, 255, 200)
WHITE = (255, 255, 255)
 
sc = pygame.display.set_mode((800, 600))
 
card = Card("qq","qq",(100,200),False)
card2 = Card("qq","qq",(100,200),True)
card3 = Card("qq","qq",(100,200),True)
 
rect = card.rect
rect2 = card2.rect
rect3 = card3.rect

print(rect.width, rect.height)  # 100
print(rect.x, rect.y)  # 0 0
 
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
 
    sc.fill(GREEN)
    sc.blit(card.image, rect)
    sc.blit(card2.image, rect2)
    sc.blit(card3.image, rect3)
    pygame.display.update()
 
    rect.x += 1
    rect2.x += 5
    rect3.y += 1
 
    pygame.time.delay(20)