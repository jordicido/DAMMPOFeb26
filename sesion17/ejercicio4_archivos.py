def copiar_archivo(original, copia):
    contenido = ""
    try:
        with open(original, "r") as archivo:
            contenido = archivo.readlines()
    except FileNotFoundError as error:
        print(f"Error {error}")
    else:
        with open(copia, "w") as archivo:
            archivo.writelines(contenido)

def main():
    copiar_archivo("sesion17/nombres.txt", "sesion17/copia_nombres.txt")

if __name__ == "__main__":
    main()