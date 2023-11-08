import pygame
from network import Network
from player import Player
width = 700
height = 700
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


def redrawWindow(win,player, player2, player3, player4):
    win.fill((255,255,255))
    if player.x<0:
        player.x=width-player.width
    if player.x>width-player.width:
        player.x=0       
    if player.y<0:
        player.y=width-player.height
    if player.y>width-player.height:
        player.y=0
    player.draw(win)
    if player2!=None:
        player2.draw(win)
    if player3!=None:
        player3.draw(win)
    if player4!=None:
        player4.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()
    player_count=0

    while run:
        clock.tick(60)
        player_count = n.send(p)[0]
        match player_count:
            case 2:
                p2 = n.send(p)[1]
                p3 = None
                p4 = None
            case 3:
                p2 = n.send(p)[1]
                p3 = n.send(p)[2]
                p4 = None
            case 4:
                p2 = n.send(p)[1]
                p3 = n.send(p)[2]
                p4 = n.send(p)[3]
            case _:
                p2=None
                p3=None
                p4=None


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win, p, p2, p3, p4)

main()