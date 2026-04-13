# Si pongo un 6
# 0, 1, 2, 3, 4, 5, 6
numero = int(input("Introduce un número entero positivo\n"))

# range(6) -> 0-5
for i in range(numero):
    print(i, end=", ")

print(numero)
