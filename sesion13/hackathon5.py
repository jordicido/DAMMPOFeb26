# Cuenta atrás

numero = int(input("Introduce un número: "))

for i in range(numero, 0, -1):
    print(i, end="")
    if i <= 3:
        print(" ¡CORRE!", end="")
    print()
print("BOOM!")