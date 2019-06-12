# -*- coding: utf-8 -*-
"""
Created on Fri May 31 17:53:25 2019

@author: ADRIAN PAREDES, CESAR GUILLÉN, MIGUEL OLÓRTEGUI, DIEGO GUTIERREZ
"""
import msvcrt
import battleship_funciones
import random
trial=int(input("Ingrese el número de veces a jugar, debe ser mayor a 0."))
while trial>0:
    #Código del juego
    game_size=10
    while game_size>8 or game_size<4:
        game_size=int(input("Ingrese modalidad de juego (hasta 8x8):"))
        print()
        print("Angamos")
        print("Octubre 8, 1879")
        print("Bienvenido Almirante Grau")
        print(battleship_funciones.tablero(game_size))
        if game_size<9 and game_size>3:
            break
        game_size=game_size
    print("El largo del Huáscar es de 2x1.")
    huascar={}
    huascar[input("Ingrese columna de ubicación de la proa Huáscar: ").upper()]=int(input("Ingrese fila de ubicación de la proa del Huáscar: "))
    direccion=input("Para la popa del Huáscar escriba +x, -x, +y o -y, según sea derecha, izquierda, arriba o abajo:")

    cochrane={}
    cochrane[battleship_funciones.char_aleatorio(game_size)]=int(random.randint(1,game_size+1))
    #Ingresar el código de juego por encima de esta línea
    trial-=1

print("GAME OVER".center(100,"="))
print("PRESIONE CUALQUIER TECLA PARA SALIR".center(100,"="))
msvcrt.getch()
