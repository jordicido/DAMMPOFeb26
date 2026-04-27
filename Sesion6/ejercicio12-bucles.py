numero = int(input("Introduce un número "))
menor = numero
mayor = numero

while numero != 0:
    if numero > mayor:
        mayor = numero
    elif numero < menor:
        menor = numero
    numero = int(input("Introduce un número "))

print(f"El numero mayor es {mayor}")
print(f"El numero menor es {menor}")
