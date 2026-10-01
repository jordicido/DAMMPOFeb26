# Calculadora propina

precio = float(input("Precio: "))
propina = float(input("Propina (%): "))

precio_propina = (precio*propina)/100

print(f"Propina: {precio_propina:.2f} €")
print(f"Precio total: {(precio+precio_propina):.2f} €")