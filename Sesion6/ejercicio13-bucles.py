numero = int(input("Introduce un número (-1 para salir) "))

while numero != -1:
    cifras = 0
    copia = numero
    while copia > 0:
        copia //= 10
        cifras += 1
    print(f"El numero {numero} tiene {cifras} cifras")
    numero = int(input("Introduce un número (-1 para salir) "))

