alumno = {
    "nombre": "Alvaro",
    "edad": 21,
    "cargo": "Delegado"
}

for llave in alumno.keys():
    print(f"{llave} : {alumno[llave]}")

for valor in alumno.values():
    print(valor)

for llave, valor in alumno.items():
    print(f"{llave} : {valor}")
