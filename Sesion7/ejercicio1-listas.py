mi_lista = input("Introduce una lista de numeros separados por coma: ") # "1,2,3,4,5" -> [1, 2, 3, 4, 5]
mi_lista = [int(numero) for numero in mi_lista.split(",")]
contador = 0

for numero in mi_lista:
    contador += numero

print(f"El resultado es {contador}")