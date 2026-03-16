print("Hola clase")

numero_alumnos = int(input("Cuantos alumnos sois?"))

print(f"El numero de alumnos es {numero_alumnos}")
# 0-19 alumnos
if numero_alumnos < 20:
    alumnos_restantes = 20 - numero_alumnos
    print(f"Faltan {alumnos_restantes} alumnos para empezar la clase")
# 60-infinitos alumnos
elif numero_alumnos > 60:
    print("Hay demasiada gente")
# 20-60 alumnos
else:
    print("Vamos a empezar la clase")

print("Fin del programa")