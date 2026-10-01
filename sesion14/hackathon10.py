lista_prods = []
lista_precios = []

num_productos = int(input("Cantidad de productos que quieres introducir: "))
for i in range(num_productos):
    producto = input(f"Producto {i+1}: ")
    precio = float(input("Precio: "))
    lista_prods.append(producto)
    lista_precios.append(precio)

subtotal = sum(lista_precios)
descuento = 0
indice_mayor = lista_precios.index(max(lista_precios))
print(f"Productos: {", ".join(lista_prods)}")
print(f"Subtotal: {subtotal:.2f}€")
if subtotal >= 50:
    descuento = subtotal*0.1
    print(f"Descuento: {descuento:.2f}€")
print(f"Total: {subtotal-descuento:.2f}€")
print(f"Más caro: {lista_prods[indice_mayor]} ({lista_precios[indice_mayor]}€)")
#los de daw son mejores a todos menos a  y Valeria, pero por detras aun de los de DAW