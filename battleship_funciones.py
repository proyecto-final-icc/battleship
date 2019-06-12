# -*- coding: utf-8 -*-
"""
Created on Fri May 31 18:40:59 2019

@author: ADRIAN PAREDES, CESAR GUILLÉN, MIGUEL OLÓRTEGUI, DIEGO GUTIERREZ
"""
#funciones
def tablero(x):
    if x>8:
        return " ERROR AL IMPRIMIR EL TABLERO, INGRESE UN VALOR VÁLIDO"
    if x<4:
        return " EL TAMAÑO MÍNIMO ES 4X4, INGRESE UN VALOR VÁLIDO"
    columnas=["A","B","C","D","E","F","G","H"]
    filas=[0,1,2,3,4,5,6,7,8]
    for z in range (0,x+1):
        for i in range (0,x):
            if z==0:
                print(columnas[i], end=" ")
            else:
                print ("o", end=" ")
        if z>=1:
            print(filas[z])
        else:
            print()
    return ""

def char_aleatorio(x):
    columnas=["A","B","C","D","E","F","G","H"]
    import random
    return columnas[random.randint(0,x)]

def popa(x):
    if x=="+x":
        columnas=[chr(i) for i in range(97,y)]
