# 5! = 5*4*3*2*1
def factorial(numero):
    resultado = 1
    for i in range(1, numero+1):
        resultado *= i
    return resultado

numero = int(input("Introduce un numero entero positivo: "))
print(f"El factorial de {numero} es {factorial(numero)}")