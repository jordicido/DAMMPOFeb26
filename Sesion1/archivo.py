# un comentario de linea UnicodeWarning

"""
    Esto
    else
    un comentario
    multilinea
"""

print("La variable ahora es 10")
variable = 10
print(type(variable))
print("La variable ahora es Jordi")
variable = "Jordi"
print(type(variable))
print("La variable ahora es True")
variable = True
print(type(variable))
print("La variable ahora es 1.1")
variable = 1.1
print(type(variable))

# En Python la convención snake_case
nombre = "Jordi"
primer_apellido = "Cidoncha"
segundo_apellido = "Navarrete"

# En Java se usa la convención camelCase -> primerApellido

edad = "38"
edad_entero = int(edad)
print("El tipo de dato de la variable edad es:")
print(type(edad))
print("El tipo de dato de la variable edad_entero es:")
print(type(edad_entero))

nota = 9.9
nota_entero = int(nota)
print("Mi nota en el examen es:")
print(nota_entero)

numero_alumnos = 13
numero_alumnos_texto = str(numero_alumnos)
print("el numero de alumnos en esta clase es:")
print(numero_alumnos_texto)


# SALIDA Y ENTRADA DE DATOS

# nombre = input("Como te llamas?\n")
# edad = int(input("Cual es tu edad?\n"))

# print(f"Tu nombre es {nombre} y tu edad es {edad}")
# print(f"El tipo de dato de la variable edad es {type(edad)}")


# Quiero que me hagáis un programa que:
# 1 - Pregunte el ciclo y el módulo que estais dando ahora
# 2 - Pregunte el número de alumnos conectados
# Con eso, imprimir un mensaje personalizado con todos esos datos

ciclo = input("Que ciclo estas cursando?\n")
modulo = input("Que modulo estas dando?\n")
alumnos = int(input("Cuantos alumnos hay conectados?\n"))

print(f"Estás cursando el ciclo de {ciclo}, estás en clase de {modulo} y hay {alumnos} alumnos conectados")
