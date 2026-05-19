def es_primo(numero):
    if numero < 2:
        return False
    
    for i in range(2, numero):
        if numero % i == 0:
            return False
    
    return True

numero = int(input("Introduce un numero entero positivo: "))
print(f"{numero} es primo? {es_primo(numero)}")