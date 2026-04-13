numero = int(input("Introduce un número entero positivo\n"))
contador = 0

for i in range(0, numero+1, 2):
    contador += 1

print(f"El numero de pares es: {contador}")
