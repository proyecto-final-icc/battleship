# -*- coding: utf-8 -*-
"""
Created on Fri May 31 17:53:25 2019
@author: ADRIAN PAREDES, CESAR GUILLÉN, MIGUEL OLÓRTEGUI, DIEGO GUTIERREZ
"""
import msvcrt
import battleship_funciones
import random
trial=int(input("Ingrese el número de veces a jugar, debe ser mayor a 0:"))
while trial>0:
    #Código del juego
    game_size=30
    while game_size>26 or game_size<4:
        game_size=int(input("Ingrese modalidad de juego (hasta 26x26):"))
        print(" ", "Angamos".center(100,"="),"Octubre 8, 1879".center(100,"="),"Bienvenido Almirante Grau".center(100,"="), " ", end="\n")
        print(battleship_funciones.tablero(game_size))
        if game_size<27 and game_size>3:
            break
        game_size=game_size
    print("El largo del Huáscar es de 2x1.")
    huascar={}
    huascar[input("Ingrese columna de ubicación de la proa Huáscar: ").upper()]=int(input("Ingrese fila de ubicación de la proa del Huáscar: "))
    direccion=input("Para la popa del Huáscar escriba +x, -x, +y o -y, según sea derecha, izquierda, arriba o abajo:")
    cochrane={}
    cochrane[battleship_funciones.char_aleatorio(game_size)]=int(random.randint(1,game_size+1))
    #Empieza el juego
    turno=True #True(banderita)->Empieza el usuario
    ataque_enemigo={}
    ataque_usuario={}
    intersección=set(ataque_enemigo.items() and ataque_usuario.items())
    while len(intersección)<2:
        if turno==True:
            print("Tu turno de atacar:")
            ataque_usuario[str(input("Ingrese columna a atacar:").upper())]=int(input("Ingrese fila a atacar:"))
            turno=False
        elif turno==False:      
            print("Turno de la computadora")
            ataque_enemigo[battleship_funciones.char_aleatorio(game_size)]=int(random.randint(1,game_size+1))
            print("Te atacaron en:", ataque_enemigo)
            turno=True
    if huascar in ataque_enemigo:
        print("Ganaste")
    elif cochrane in ataque_usuario:
        print("Perdiste")
    #Ingresar el código de juego por encima de esta línea
    trial-=1
print("GAME OVER".center(100,"="), "PRESIONE CUALQUIER TECLA PARA SALIR".center(100,"="), end="\n" )
print()
msvcrt.getch()
