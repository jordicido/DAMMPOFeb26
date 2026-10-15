# Manejo de archivos
try:
    datos = open("sesion16/datos-alumnos.txt", "r+")
    info = datos.readlines()
    cabecera = info[0:2]
    alumnos = info[2:]
    alumnos.sort()
    datos.seek(0)
    datos.writelines(cabecera+alumnos)
    
except FileNotFoundError as error:
    print(f"Error: {error}")

print("Fin del programa")