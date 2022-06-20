import sys
from pygame.locals import *
from pygame import *
import pygame
from configuracion import *
import menu


def about():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO,ALTO),0,32)

    background2 = pygame.image.load("static/about.png").convert()
    myfont2 = font.SysFont("Impact", 30)
    redirectMenu = Rect(670, 40, 80, 40)

    while True:
        ventana.blit(background2, [0, 0])

        for event in pygame.event.get():
        #cerrar texto
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()

            if (keys[pygame.K_ESCAPE]):
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if redirectMenu.collidepoint(mouse.get_pos()):
                        menu.funcionMenu()

        if redirectMenu.collidepoint(mouse.get_pos()):

            draw.rect(ventana, (186, 189, 162), redirectMenu, 0)
        else:
            draw.rect(ventana, (70, 189, 34), redirectMenu, 0)
        texto = myfont2.render("Menu", True, (255, 255, 255))
        ventana.blit(texto, (675,40))

        pygame.display.flip()