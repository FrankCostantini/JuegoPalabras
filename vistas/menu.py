from configuracion import *
from pygame import *
import sys
from pygame.locals import *
import pygame

pygame.init()
ventana = pygame.display.set_mode((640,480),0,32)

background = pygame.image.load("../static/background.png").convert()
####

miFuente = pygame.font.Font(None,80)
titulo = miFuente.render("     Juego de palabras      ",0,(200,60,80),(100,100,100))

#boton de jugar
#boton de informacion sobre el juego
#boton de quit
myfont=font.SysFont("Calibri",30)

jugar=Rect(100,100,150,50)



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
    #boton Jugar
    draw.rect(ventana, (70, 189, 34), jugar, 0)
    texto=myfont.render("Jugar",True,(220,220,220))

    ventana.blit(texto,(100+(jugar.width - texto.get_width())/2,100))

    pygame.display.flip()
    mouse = pygame.mouse.get_pos()



