from pygame import *
import sys
from pygame.locals import *
import pygame
from vistaNiveles import *
import informacion
from funcionesVACIAS import *
from extras import *
from configuracion import *

def pintar(screen, palabraUsuario):


    defaultFont=font.SysFont("Impact", 40)
    defaultFontGrande= font.SysFont("Impact", 40)
    #Linea Horizontal
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

    #muestra lo que escribe el jugador
    screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_TEXTO), (190, 570))


pygame.init()
ventana = pygame.display.set_mode((800, 600), 0, 32)
background = pygame.image.load("static/action.png").convert()

miFuente = pygame.font.Font(None, 100)
# titulo = miFuente.render("Juego de palabras", 0, (200, 60, 80), (100, 100, 100))

# boton de jugar
# boton de informacion sobre el juego
# boton de quit




palabra=""

while True:
    ventana.blit(background, [0, 0])

    for event in pygame.event.get():
        # cerrar texto
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()

        if (keys[pygame.K_ESCAPE]):
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            letra = dameLetraApretada(event.key)
            palabra += letra  # es la palabra que escribe el usuario
            if event.key == K_BACKSPACE:
                palabra = palabra[0:len(palabra) - 1]

    pintar(ventana,palabra)

