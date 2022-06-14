from principal import *
from configuracion import *
import random
import pyphen
import math

LONG_MIN=4

def lectura(archivo, salida):
    salida.append(archivo)


def nuevaPalabra(lista):
    azar = random.randint(0,len(lista))

    print(lista[azar])


def silabasTOpalabra(silaba):
    ind="- "
    var=""
    for i in range(len(silaba)):
        if silaba[i] not in ind:
            var= var + silaba[i]

    return var

def palabraTosilaba(palabra):
    a = pyphen.Pyphen(lang='es')
    return a.inserted(palabra)


def esCorrecta(palabraEnSilabasEnPantalla, palabra):
    if silabasTOpalabra(palabraEnSilabasEnPantalla) == silabasTOpalabra(palabra) and len(palabra) > LONG_MIN:
        return True
    else:
        return False

def puntaje(palabraEnSilabas,palabra):
    if esCorrecta(palabraEnSilabas,palabra):
      return 5
    else:
        return -5

print(silabasTOpalabra("pe pe ju-chu"))
