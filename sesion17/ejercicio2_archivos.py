def contar_lineas_y_palabras(contenido):
    num_lineas = len(contenido)
    num_palabras = 0
    for linea in contenido:
        num_palabras += len(linea.split())
    return num_lineas, num_palabras

try:
    with open("sesion17/ejemplo.txt", "r") as archivo:
        contenido = archivo.readlines()
        num_lineas, num_palabras = contar_lineas_y_palabras(contenido)
        print(f"El archivo tiene {num_lineas} lineas y {num_palabras} palabras")
except FileExistsError as error:
    print(f"Error: {error}")