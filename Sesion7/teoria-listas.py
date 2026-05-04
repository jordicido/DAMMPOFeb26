# Teoria listas
# Las listas son colecciones ordenadas y mutables de elementos.

# Inicializar una lista

mi_lista = [1, 2, 3]
mi_lista2 = []
mi_lista3 = list()
mi_lista4 = list([2, 3, 4])

# Para mostrar los valores de una lista
print(mi_lista)


# obtener el valor de un elemento de la lista
print(mi_lista[1])

# para modificar un elemento de la lista, tambien debo usar el índice
mi_lista[1] = 5
print(mi_lista)

# Para acceder al último elemento de una lista podemos usar los índices negativos
print(mi_lista[-1])

# append(): Agrega un elemento al final de la lista.
mi_lista.append(4)
print(mi_lista)
mi_lista.append(3)
mi_lista.append(4)

# insert(): Inserta un elemento en una posición específica de la lista.
mi_lista.insert(0, 24)
print(mi_lista)

# remove(): Elimina el primer elemento con el valor especificado.
mi_lista.remove(4)
print(mi_lista)

# pop(): Elimina y devuelve el último elemento de la lista (o el elemento en la posición especificada).
print(mi_lista.pop())
print(mi_lista)

#sort(): Ordena los elementos de la lista en orden ascendente.
mi_lista.sort()
print(mi_lista)

# reverse(): Invierte el orden de los elementos en la lista.
mi_lista.reverse()
print(mi_lista)

# len(): Devuelve la longitud de la lista (número de elementos).
print(len(mi_lista))
