numero = int(input("Introduce un número (0 para acabar): "))
sumador = 0

while numero != 0:
    sumador += numero
    numero = int(input("Introduce un número (0 para acabar): "))

print(f"El resultado final es {sumador}")

