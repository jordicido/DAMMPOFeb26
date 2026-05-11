'''
mi_lista = input("Introduce una lista de numeros separados por coma: ").split(",")
lista_enteros = []
for numero in mi_lista:
    lista_enteros.append(int(numero)) 
'''
mi_lista = [int(num) for num in input("Introduce una lista de numeros separados por coma: ").split(",")]
# [1, 2, 3, 4, 5]
# menor = mi_lista[0]
# mayor = mi_lista[0]

# for numero in mi_lista:
#     if numero > mayor:
#         mayor = numero
#     if numero < menor:
#         menor = numero

print(f"El mayor es {max(mi_lista)} y el menor es {min(mi_lista)}")

