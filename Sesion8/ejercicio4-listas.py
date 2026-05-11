mi_lista1 = [int(num) for num in input("Introduce una lista de numeros separados por coma: ").split(",")]
mi_lista2 = [int(num) for num in input("Introduce otra lista de numeros separados por coma: ").split(",")]

if len(mi_lista1) != len(mi_lista2):
    print("Error: La longitud de las listas no es igual")
else:
    suma = []
    for i in range(len(mi_lista1)):
        suma.append(mi_lista1[i] + mi_lista2[i])

    print(f"Lista resultante: {suma}")