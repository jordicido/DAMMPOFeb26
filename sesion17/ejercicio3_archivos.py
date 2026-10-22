def crear_archivo(nombre_archivo, datos):
    with open(nombre_archivo, "w") as archivo:
        for nombre in datos:
            archivo.write(nombre + "\n")
    
def main():
    lista_nombres = input("Introduce los nombres que quieras añadir separados por coma\n").split(",")
    crear_archivo("sesion17/nombres.txt", lista_nombres)

if __name__ == "__main__":
    main()