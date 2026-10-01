# Calculadora de tiempo

total_segundos = int(input("Introduce segundos: "))

# segundos = 3932
horas = total_segundos // 3600 # 1h
resto_segundos = total_segundos % 3600
# resto_segundos = 332
minutos = resto_segundos // 60 # 5m
segundos = resto_segundos % 60
# segundos = 32s

print(f"{horas} h {minutos} min {segundos} s")