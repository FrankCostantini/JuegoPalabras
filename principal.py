#! /usr/bin/env python
import time
import os, random, sys

import menu
from niveles import *
import pygame
import pyphen
from configuracion import *
from funcionesSeparador import *
from informacion import *
from extras import *
from niveles import *
from funcionesVACIAS import *
import niveles
from menu import *
import time


#Funcion principal

def main(num):
        pygame.mixer.quit()


        myfont2 = font.SysFont("Impact", 40)
        redirectMenu = Rect(670, 40, 80, 40)
        nivel= num

        TIEMPO_MAX = dificultadTiempo(nivel)

        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        #pygame.mixer.init()

        #Preparar la ventana
        pygame.display.set_caption("El juego del Mago Goma...")
        screen = pygame.display.set_mode((ANCHO, ALTO))

        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial

        puntos = 0
        palabra = ""
        lemarioEnSilabas=[]
        listaPalabrasDiccionario=[]

        archivo= open("lemario.txt", "r")

        #lectura del diccionario
        lectura(archivo, listaPalabrasDiccionario)


        #elige una al azar
        """
        npal=nuevaPalabra(listaPalabrasDiccionario)

        if cuentaSilabas(npal) <= 2 and nivel == 0:
            palabraEnPantalla = nuevaPalabra(listaPalabrasDiccionario)
        elif cuentaSilabas(npal) > 3 and cuentaSilabas(npal) <= 4 and nivel == 1:
            palabraEnPantalla = nuevaPalabra(listaPalabrasDiccionario)
        elif cuentaSilabas(npal) > 5 and nivel == 2:
            palabraEnPantalla = nuevaPalabra(listaPalabrasDiccionario)
        else:
            palabraEnPantalla = nuevaPalabra(listaPalabrasDiccionario)
    """

        palabraEnPantalla=nuevaPalabra(listaPalabrasDiccionario)


        dibujar(screen,palabra,palabraEnPantalla, puntos,segundos)

        while segundos > fps/1000:
            draw.rect(screen, (186, 189, 162), redirectMenu, 10)

            texto = myfont2.render("Menu", True, (255, 255, 255))
            screen.blit(texto, (675, 40))

        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()


            if True:
                fps = 3

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    palabra += letra #es la palabra que escribe el usuario
                    if e.key == K_BACKSPACE:
                        palabra = palabra[0:len(palabra)-1]
                    if e.key == K_RETURN:

                        #pasa la palabra a silabas
                        palabraEnPantallaEnSilabas=palabraTOsilaba(palabraEnPantalla)
                        if esCorrecta(palabraEnPantallaEnSilabas, palabra):
                            puntos+=5

                        else:
                            puntos-=1

                        if nivel == valor(nivel) and esCorrecta(palabraEnPantallaEnSilabas, palabra):
                            TIEMPO_MAX += adicional(nivel)
                        else:
                            TIEMPO_MAX -= descuento(nivel)



                        #elige una al azar
                        palabraEnPantalla=nuevaPalabra(listaPalabrasDiccionario)

                        palabra = ""

            segundos = (TIEMPO_MAX - pygame.time.get_ticks() / 1000)


            #Limpiar pantalla anterior
            screen.fill(COLOR_FONDO)

            #Dibujar de nuevo
            dibujar(screen, palabra, palabraEnPantalla, puntos,segundos)

            pygame.display.flip()

        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                if e.type == MOUSEBUTTONDOWN and e.button == 1:
                    if redirectMenu.collidepoint(mouse.get_pos()):
                        menu.funcionMenu()

        archivo.close()
#Programa Principal ejecuta Main
if __name__ == "__main__":
    funcionMenu()


