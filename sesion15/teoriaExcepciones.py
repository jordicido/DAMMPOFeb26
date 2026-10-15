

while True:
    print("Menu")
    print("Opcion 1")
    print("Opcion 2")
    print("Opcion 3")
    try:
        opcion = int(input("Escoge una opcion: "))
        if opcion < 1 or opcion > 3:
            raise ValueError("Escoge una opcion entre 1 y 3")

    except ValueError as e:
        print(f"Error: {e}")