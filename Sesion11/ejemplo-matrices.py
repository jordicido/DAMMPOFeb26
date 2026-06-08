matriz = []
contador = 1
for i in range(3):
    lista = []
    for j in range(3):
        lista.append(contador)
        contador += 1
    matriz.append(lista)

print(matriz)