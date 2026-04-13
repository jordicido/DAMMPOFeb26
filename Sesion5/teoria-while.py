# Sumar los numeros que vaya introduciendo el usuario hasta ingresar un número negativo
resultado = 0
numero = int(input("Introduce un número a sumar (numero negativo para salir)"))

while numero >= 0:
    resultado += numero
    numero = int(input("Introduce un número a sumar (numero negativo para salir)"))

print(resultado)
