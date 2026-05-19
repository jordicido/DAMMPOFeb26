import math

def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area

radio = float(input("Introduce el radio del circulo: "))
area = calcular_area_circulo(radio)
print(f"El area de un circulo de radio {radio} es {area}")