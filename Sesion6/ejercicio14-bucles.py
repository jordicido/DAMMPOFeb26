numero = int(input("Introduce un número "))
primo = True

for i in range(2, numero):
    if numero%i == 0:
        primo = False
        break

if primo:
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")
