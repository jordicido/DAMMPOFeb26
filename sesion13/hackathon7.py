# multiples de 3

limite = int(input("Introduce límite: "))
cantidad = 0
suma = 0

print("Múltiplos: ", end="")
for i in range(1, limite+1):
    if i % 3 == 0:
        print(i, end=" ")
        cantidad += 1
        suma += i
print()
print(f"Cantidad: {cantidad}")
print(f"Suma: {suma}")