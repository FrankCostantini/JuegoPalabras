from configuracion import *


def valor(nivel):
    if nivel == 0:
        val = 0
    elif nivel == 1:
        val = 1
    elif nivel == 2:
        val = 2
    return val

def dificultadTiempo(nivel):
    if nivel == 0:
        TIEMPO_MAX = 91
    elif nivel == 1:
        TIEMPO_MAX = 61
    elif nivel == 2:
        TIEMPO_MAX = 41
    return TIEMPO_MAX

def adicional(nivel):
    ad = 0
    if nivel == 0:
        ad = 3
    elif nivel == 1:
        ad = 2
    elif nivel == 2:
        ad = 1
    return ad

def descuento(nivel):
    des = 0
    if nivel == 0:
        des = 0
    elif nivel == 1:
        des = 1
    elif nivel == 2:
        des = 2
    return des