
try:
    with open("sesion17/ejemplo.txt", "r") as archivo:
        print(f"El archivo contiene {len(archivo.readlines())} lineas")
except FileNotFoundError as error:
    print(f"Error: {error}")