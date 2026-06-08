def imprimir_inventario():
    print("INVENTARIO:")
    print()
    for producto, cantidad in inventario.items():
        print(f"{producto} -> {cantidad}")   

def consultar_producto(producto):
    if producto in inventario:
        unidades = inventario.get(producto)
        print(f"{producto} : {unidades} {"unidades" if unidades > 1 else "unidad"}")
    else:
        print("Ese producto no existe en el inventario.")

def añadir_unidades(producto, unidades):
    if producto in inventario:
        inventario[producto] += unidades
    print(f"El producto {producto} tiene {inventario[producto]} {"unidades" if inventario[producto] > 1 else "unidad"}")

inventario = {
    "pocion": 3,
    "espada": 1,
    "escudo": 2
}

while True:
    print("""
----- INVENTARIO DEL MERCADER -----

1. Ver inventario
2. Consultar producto
3. Añadir unidades
4. Añadir producto
5. Vender producto
6. Salir
""")
    opcion = int(input("Escoge una opción: "))
    match opcion:
        case 1:
            imprimir_inventario()      
        case 2:
            producto = input("Introduce el producto que quieres consultar: ").lower()
            consultar_producto(producto)
        case 3:
            producto = input("Introduce el producto para añadir unidades: ").lower()
            unidades = int(input("Cuantas unidades quieres añadir? "))
            añadir_unidades(producto, unidades)
        case 4:
            producto = input("Introduce el producto para añadir: ").lower()
            unidades = int(input("Cuantas unidades quieres añadir? "))
            if producto in inventario:
                inventario[producto] += unidades
            else:
                inventario[producto] = unidades
            print(f"El producto {producto} tiene {inventario[producto]} {"unidades" if inventario[producto] > 1 else "unidad"}")
        case 5:
            producto = input("Introduce el producto para vender: ").lower()
            unidades = int(input("Cuantas unidades quieres vender? "))
            if producto in inventario:
                if unidades > inventario[producto]:
                    print(f"Stock insuficiente: El producto {producto} tiene {inventario[producto]} {"unidades" if inventario[producto] > 1 else "unidad"} en stock")
                else:
                    inventario[producto] -= unidades
                    print(f"El producto {producto} tiene {inventario[producto]} {"unidades" if inventario[producto] > 1 else "unidad"}")
                    if inventario[producto] == 0:
                        inventario.pop(producto)
            else:
                print("Ese producto no existe en el inventario.")
        case 6:
            print("Adiós!")
            break

