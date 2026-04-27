import random

numero_aleatorio = random.randint(1, 100)
numero_escogido = int(input("Elige un número del 1 al 100: "))

while numero_escogido != numero_aleatorio:
    if numero_escogido > numero_aleatorio:
        print("Escoge un número menor")
    else:
        print("Escoge un número mayor")
    numero_escogido = int(input("Elige un número del 1 al 100: "))

print(f"Correcto, el número secreto era {numero_aleatorio}")