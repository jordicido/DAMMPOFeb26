def anadir_pais(entrada):
    entrada_dict = entrada.split("-") 
    atlas[entrada_dict[0]] = entrada_dict[1]


atlas = {}
entrada = input("Introduce información en formato PAIS-CAPITAL: ")

while entrada != "FIN INSERCIONES":
    anadir_pais(entrada)
    entrada = input("Introduce información en formato PAIS-CAPITAL: ")

while True:
    print("Qué quieres hacer ahora?")
    print("1. Añadir otro país")
    print("2. Consultar una capital")
    print("3. Salir")
    opcion = int(input())
    match opcion:
        case 1:
            entrada = input("Introduce información en formato PAIS-CAPITAL: ")
            anadir_pais(entrada)
        case 2:
            entrada = input("Introduce la capital a consultar: ").upper()
            if entrada in atlas:
                print(f"La capital de {entrada} es {atlas[entrada]}")
            else:
                print("No existe ese país en el diccionario")
        case 3:
            print("Adiós")
            break