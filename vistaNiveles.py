import menu
from configuracion import *
from pygame import *
import sys
from pygame.locals import *
import pygame
import principal
import niveles
import nivel2
from funcionesVACIAS import *



def vistaNivels():

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO,ALTO),0,32)

    background2 = pygame.image.load("static/background3.jpg").convert()
    myfont = font.SysFont("Impact", 40)
    myfont2= font.SysFont("Impact",30)
    facil = Rect(100,250, 150, 80)
    medio = Rect(350,250, 150, 80)
    dificil = Rect(600,250, 150, 80)

    redirectMenu=Rect(670,40,80,40)

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
                if facil.collidepoint(mouse.get_pos()):

                    principal.main()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if medio.collidepoint(mouse.get_pos()):

                    principal.main()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if dificil.collidepoint(mouse.get_pos()):

                    principal.main()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if redirectMenu.collidepoint(mouse.get_pos()):
                    menu.funcionMenu()

        #redirectMenu

        if redirectMenu.collidepoint(mouse.get_pos()):

            draw.rect(ventana, (186, 189, 162), redirectMenu, 0)
        else:
            draw.rect(ventana, (70, 189, 34), redirectMenu, 0)
        texto = myfont2.render("Menu", True, (255, 255, 255))
        ventana.blit(texto, (675, 40))





        # pintar boton facil
        if facil.collidepoint(mouse.get_pos()):

            draw.rect(ventana, (186, 189, 162), facil, 0)
        else:
            draw.rect(ventana, (70, 189, 34), facil, 0)
        texto = myfont.render("Facil", True, (255, 255, 255))
        ventana.blit(texto, (130,265))

        # pintar boton medio
        if medio.collidepoint(mouse.get_pos()):

            draw.rect(ventana, (186, 189, 162),medio, 0)
        else:
            draw.rect(ventana, (70, 189, 34),medio, 0)
        texto = myfont.render("Medio", True, (255, 255, 255))
        ventana.blit(texto, (374, 265))

        # pintar boton dificil
        if dificil.collidepoint(mouse.get_pos()):

            draw.rect(ventana, (186, 189, 162),dificil, 0)
        else:
            draw.rect(ventana, (70, 189, 34),dificil, 0)
        texto = myfont.render("Dificil", True, (255, 255, 255))
        ventana.blit(texto, (628,265))


        pygame.display.flip()