from configuracion import *
import pygame, sys
from pygame.locals import *
pygame.init()
ventana = pygame.display.set_mode((640,480),0,32)

background = pygame.image.load("../static/background.png").convert()
####

miFuente = pygame.font.Font(None,80)
titulo = miFuente.render("     Juego de palabras      ",0,(200,60,80),(100,100,100))

#boton de quit

while True:
    ventana.blit(background, [0, 0])
    ventana.blit(titulo,(0,0)).center



    for event in pygame.event.get():
        #cerrar texto
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()

        if (keys[pygame.K_ESCAPE]):
            pygame.quit()
            sys.exit()




    pygame.display.flip()
    mouse = pygame.mouse.get_pos()



