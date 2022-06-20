
from pygame import *
import sys
from pygame.locals import *
import pygame
from vistaNiveles import *
import informacion
from funcionesVACIAS import *
from extras import *
from configuracion import *


def funcionMenu():

    pygame.init()
    ventana = pygame.display.set_mode((800,600), 0, 32)
    background = pygame.image.load("static/action.png").convert()

    miFuente = pygame.font.Font(None, 100)
    #titulo = miFuente.render("Juego de palabras", 0, (200, 60, 80), (100, 100, 100))

    # boton de jugar
    # boton de informacion sobre el juego
    # boton de quit
    myfont = font.SysFont("Impact", 40)

    pygame.mixer.music.load("song/Sonido.mp4")
    pygame.mixer.music.play()
    jugar = Rect(133, 175, 150, 50)
    about = Rect(100, 278, 220, 50)
    salir = Rect(133, 378, 150, 50)

    while True:
        ventana.blit(background, [0, 0])
        #ventana.blit(titulo, (0, 0))

        for event in pygame.event.get():
            # cerrar texto
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()

            if (keys[pygame.K_ESCAPE]):
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if jugar.collidepoint(mouse.get_pos()):
                    vistaNivels()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if about.collidepoint(mouse.get_pos()):
                    informacion.about()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if salir.collidepoint(mouse.get_pos()):
                    pygame.quit()

        # pintar boton jugar
        if jugar.collidepoint(mouse.get_pos()):

            draw.rect(ventana, (186, 189, 162), jugar, 0)
        else:
            draw.rect(ventana, (70, 189, 34), jugar, 0)
        texto = myfont.render("Jugar", True, (255, 255, 255))
        ventana.blit(texto, (163, 172))

        # pintar boton about
        if about.collidepoint(mouse.get_pos()):

            draw.rect(ventana, (186, 189, 162), about, 0)
        else:
            draw.rect(ventana, (70, 189, 34), about, 0)
        texto = myfont.render("Como Jugar", True, (255, 255, 255))
        ventana.blit(texto, (115, 277))

        # pintar boton salir
        if salir.collidepoint(mouse.get_pos()):
            draw.rect(ventana, (186, 189, 162), salir, 0)
        else:
            draw.rect(ventana, (70, 189, 34), salir, 0)
        texto = myfont.render("Salir", True, (255, 255, 255))
        ventana.blit(texto, (170, 375))

        pygame.display.flip()







