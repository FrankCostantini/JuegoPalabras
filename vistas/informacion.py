import sys
from pygame.locals import *
import pygame
from configuracion import *

def about():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO,ALTO),0,32)

    background2 = pygame.image.load("../static/about.png").convert()

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

        pygame.display.flip()