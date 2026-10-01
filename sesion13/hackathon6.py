# Adivina el numero
import random

secreto = random.randint(1,100)
intento = int(input("Di un numero entre 1 y 100: "))
intentos = 1

while secreto != intento:
    if (intento > secreto):
        print("Demasiado alto!")
    else:
        print("Demasiado bajo!")
    intento = int(input("Fallaste! Di un numero entre 1 y 100: "))
    intentos += 1

print(f"Correcto! El numero secreta era el {secreto}")
print(f"Intentos: {intentos}")