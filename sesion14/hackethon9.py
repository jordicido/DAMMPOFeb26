# Inventario de videojuego

inventario = {"espada": 1, "poción": 6, "escudo": 2}

opcion = 0
while opcion != 5:
    print('''
Qué quieres hacer?
1. Ver inventario
2. Añadir objeto
3. Usar objeto
4. Buscar objeto
5. Salir
    ''')
    opcion = int(input(""))
    match(opcion):
        case 1:
            print("Inventario:")
            i = 1
            for item, cantidad in inventario.items():
                print(f"{i}. {cantidad} {item}")
                i += 1
        case 2:
            item = input("Qué objeto quieres añadir?\n")
            if item in inventario.keys():
                inventario[item] += 1
            else:
                inventario[item] = 1
        case 3:
            item = input("Qué objeto quieres usar?\n")
            if item in inventario:
                cantidad = int(input(f"Qué cantidad de {item} quieres usar?\n"))
                if cantidad <= inventario[item]:
                    inventario[item] -= cantidad
                    print(f"Has usado {cantidad} {item}")
                else:
                    print(f"No hay cantidad suficiente de {item} en el inventario")
            else:
                print(f"{item} no se encuentra en el inventario")
        case 4:
            item = input("Qué objeto quieres buscar?\n")
            if item in inventario.keys():
                cantidad = inventario[item]
                if cantidad > 1:
                    print(f"Hay {cantidad} unidades de {item}")
                else:
                    print(f"Hay 1 unidad de {item}")
            else:
                print(f"{item} no se encuentra en el inventario")
        case 5:
            print("Au revoir")
