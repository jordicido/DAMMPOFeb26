numero = int(input("Introduce un número entero\n"))

if numero % 3 == 0 and numero % 5 == 0:
    print("El número es divisible entre 3 y 5")
elif numero % 3 == 0:
    print("El número es divisible entre 3")
elif numero % 5 == 0:
    print("El número es divisible entre 5")
else:
    print("Número no es múltiple de 3 ni de 5")