evaluaciones = int(input("Cuantas evaluaciones quieres evaluar? "))

for i in range(1, evaluaciones+1):
    numero_notas = 0
    suma_total = 0
    nota = float(input(f"Dime una nota de la evaluación {i}: "))
    while nota != -1:
        suma_total += nota
        numero_notas += 1
        nota = float(input(f"Dime una nota de la evaluación {i}: "))
    print(f"La nota media de la evaluación {i} es {suma_total/numero_notas}")