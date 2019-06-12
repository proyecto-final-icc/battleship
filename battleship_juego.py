# -*- coding: utf-8 -*-
"""
Created on Fri May 31 17:53:25 2019

@author: ADRIAN PAREDES, CESAR GUILLÉN, MIGUEL OLÓRTEGUI, DIEGO GUTIERREZ
"""
import msvcrt
import battleship_funciones
import random
trial=2
while trial>0:
    #Código del juego
    game_size=10
    while game_size>9:
        game_size=int(input("Ingrese modalidad de juego (hasta 8x8):"))
        print("Angamos")
        print("Octubre 8, 1879")
        print("Bienvenido Almirante Grau")
        print(battleship_funciones.tablero(game_size))
        if game_size<=8:
            break
        game_size=game_size
    huascar=[" ",int]
    huascar[0]=input("Ingrese columna de ubicación del Huáscar: ").upper()
    huascar[1]=int(input("Ingrese fila de ubicación del Huáscar: "))
    esmeralda=["",int]
    esmeralda[0]=battleship_funciones.char_aleatorio(game_size)
    esmeralda[1]=random.randint(0,game_size)
    #Ingresar el código de juego por encima de esta línea
    trial-=1

print("GAME OVER".center(100,"="))
print("PRESIONE CUALQUIER TECLA PARA SALIR".center(100,"="))
msvcrt.getch()
