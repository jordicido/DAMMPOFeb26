# Recorre una lista de numeros y cada vez que encuentres un 6, conviertelo a 9, y cada vez que encuentros un 9, conviertelo a 6
lista_numeros =  [1,2,3,6,7,12,32,9,12,6,9,12,34,5,6,78,9,12,21,32,6]

for i in range(len(lista_numeros)):
    if lista_numeros[i] == 6:
        lista_numeros[i] = 9
    elif lista_numeros[i] == 9:
        lista_numeros[i] = 6

print(lista_numeros)