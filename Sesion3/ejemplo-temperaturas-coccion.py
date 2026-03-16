# Programa que compruebe temperaturas optimas de coccion
# de los alimentos

temperatura = float(input("Dime la temperatura en la que estas concinando el pollo\n"))

# 0-60 no se cocina
# 60-200 optima
# >200 se quema
if temperatura >= 200.0:
    print("Se quema")
elif temperatura >= 60.0:
    print("Temperatura optima")
elif temperatura < 60.0:
    print("No se cocina")
