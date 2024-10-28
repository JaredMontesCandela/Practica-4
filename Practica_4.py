# -*- coding: utf-8 -*-
"""

@author: jared
"""

import random

# Personajes - Armas - Lugares
personajes = ["Dr. Alejandro Torres", "Sra. Marta Valencia", "Sr. Pedro García", "Srta. Julia Silva", "Capitán Ricardo Ortega"]
locaciones = ["Biblioteca", "Cocina", "Jardín", "Sala de estar", "Habitación principal"]
armas = ["Cuchillo", "Revólver", "Cuerda", "Veneno", "Tubo de metal"]

# Elección aleatoria del culpable, lugar y arma
culpable = random.choice(personajes)
arma = random.choice(armas)
locacion = random.choice(locaciones)

# Mensajes de bienvenida
print("¡Bienvenido al juego de misterio de Clue!")
print("Tienes 8 intentos para adivinar al culpable, la locación y el arma del crimen.")
print("Puedes hacer preguntas para obtener pistas.\n")

# Función para dar pistas
def dar_pista(intentos_restantes):
    pista = ""
    if intentos_restantes <= 6:
        pista += f"Pista: El culpable es {'no' if random.choice([True, False]) else ''} uno de los primeros dos personajes.\n"
    if intentos_restantes <= 4:
        pista += f"Pista: La locación es {'no' if random.choice([True, False]) else ''} un espacio cerrado.\n"
    if intentos_restantes <= 2:
        pista += f"Pista: El arma es {'no' if random.choice([True, False]) else ''} algo punzante.\n"
    return pista if pista else "No hay pistas adicionales por ahora."

# Inicio del Juego Principal
intentos = 8

while intentos > 0:
    print(f"\nIntento #{8 - intentos}")
    print("¿Qué deseas preguntar o adivinar?")
    print("1. Preguntar sobre el culpable")
    print("2. Preguntar sobre la locación")
    print("3. Preguntar sobre el arma")
    print("4. Hacer una conjetura final")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        print(f"Pista: El culpable {'es' if random.choice([True, False]) else 'no es'} alguien muy respetado.")
    elif opcion == "2":
        print(f"Pista: El crimen ocurrió {'dentro de' if random.choice([True, False]) else 'fuera de'} la casa principal.")
    elif opcion == "3":
        print(f"Pista: El arma {'es' if random.choice([True, False]) else 'no es'} algo que se encuentra en una cocina.")
    elif opcion == "4":
        sospechoso = input("¿Quién crees que es el culpable?: ")
        sitio = input("¿En qué locación crees que ocurrió el crimen?: ")
        arma_sospechosa = input("¿Con qué arma crees que se cometió el crimen?: ")

        # Verifica si el jugador ha adivinado correctamente
        if sospechoso == culpable and sitio == locacion and arma_sospechosa == arma:
            print("¡Felicidades! Has resuelto el misterio.")
            print(f"El culpable era {culpable} en la {locacion} con el {arma}.")
            break
        else:
            print("No es correcto. Sigue investigando.")
            print(dar_pista(intentos))
    else:
        print("Opción no válida. Inténtalo de nuevo.")

    intentos -= 1

if intentos == 0:
    print("\nLo siento, has agotado tus intentos. ¡El misterio queda sin resolver!")
    print(f"El culpable era {culpable} en la {locacion} con el {arma}.")
