dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
numero = int(input("Introduce un número (0 para salir): "))

while numero != 0:
    print(dias_semana[numero-1])
    numero = int(input("Introduce un número (0 para salir): "))

