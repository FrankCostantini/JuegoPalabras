from principal import *
from configuracion import *
import random
import pyphen
import math

LONG_MIN=4




def dlenter(linea):
    linea2=""
    for i in range(len(linea)-1):
        linea2 += linea[i]
    return linea2



def lectura(archivo, salida):
    for linea in archivo:
        línea = archivo.readline()
        linea2 = dlenter(linea)
        salida.append(linea2)

def nuevaPalabra(lista):
    relleno = []
    var = ""
    azar = random.randint(0, len(lista))
    if lista[azar] not in relleno and  len(lista[azar]):
        var = lista[azar]
        relleno.append(lista[azar])
    else:
        azar = random.randint(0, len(lista))
    return var


def silabasTOpalabra(silaba):
    ind="- "
    var=""
    for i in range(len(silaba)):
        if silaba[i] not in ind:
            var= var + silaba[i]

    return var

def palabraTOsilaba(palabra):
    a = pyphen.Pyphen(lang='es')
    var= a.inserted(palabra)
    return var


def cambioEspacio(palabra):
    pal = ""
    for i in range(len(palabra)):
        if palabra[i] != "-":
            pal += palabra[i]
        elif palabra[i] == "-":
            pal += " "
    return pal




def esCorrecta(palabraEnSilabasEnPantalla,palabra):
    palabraGuion=palabraEnSilabasEnPantalla
    palabraEspacio=cambioEspacio(palabraEnSilabasEnPantalla)
    if palabra ==palabraGuion or palabra==palabraEspacio :
        return True
    else:
        return False



def cuentaSilabas(pal):
    cont = 0
    palabra=palabraTOsilaba(pal)
    for i in range(len(palabra)) :
        if palabra[i] == "-":
            cont += 1
    return cont




