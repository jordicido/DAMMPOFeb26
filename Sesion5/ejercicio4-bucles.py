numero = int(input("Introduce un número entero positivo\n"))
resultado = 1

for factorial in range(1,numero+1):
    resultado *= factorial

print(f"El factorial de {numero}! es {resultado}")
