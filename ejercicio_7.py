# 1 el usuario ingresa una opción

import random

def razonamiento_maquina(opciones_maquina):
    opcion_maquina = random.randint(0,2)
    return opciones_maquina[opcion_maquina]


opciones_maquina = ["piedra","papel","tijera"]

menu = """
1. Piedra
2. Papel
3. Tijera
"""



opcion_usuario_menu = "si"

while opcion_usuario_menu == "si":
    print(menu)
    opcion_usuario = input("Ingresa una opcion: ")
    respuesta = razonamiento_maquina(opciones_maquina)
    if opcion_usuario == respuesta:
        print("Fue un empate")
        print(menu)
        opcion_usuario = input("Ingresa una opcion: ")
        respuesta = razonamiento_maquina(opciones_maquina)
    else:
        
        if opcion_usuario == "piedra":
            if respuesta == "papel":
                print("El ganador es la Maquina")
            elif respuesta == "tijera":
                print("El ganador es el Usuario") 
        elif opcion_usuario == "papel":
            if respuesta == "tijera":
                print("El ganador es la Maquina")
            elif respuesta == "piedra":
                print("El ganador es el Usuario")
        elif opcion_usuario == "tijera":
            if respuesta == "papel":
                print("El ganador es el Usuario")
            elif respuesta == "piedra":
                print("El ganador es la Maquina")
    print(respuesta)            
    opcion_usuario_menu = input("Quieres seguir jugando? si/no: ")
                   