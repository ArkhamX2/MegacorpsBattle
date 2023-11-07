import pygame
from network import Network
width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

def main():
    run = True
    n = Network()
    d = n.getP()
    print(d)
    clock = pygame.time.Clock()
    player_count=0

#d={"PNum": [],"PHend": [[],[],[],[]], "BCards": [], "IsReady": [False, False, False, False]}
    
    while run:
        clock.tick(60)
        d = n.send(d)
        print(d)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        pygame.display.update()

main()