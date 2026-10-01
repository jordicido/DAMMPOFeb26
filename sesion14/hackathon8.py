# Analizador de notas

notas = [int(num) for num in input("Introduce una lista de notas separada por coma\n").split(",")]
maxima = notas[0]
minima = notas[0]
total = 0
aprobados = 0
suspendidos = 0

for nota in notas:
    if nota > maxima:
        maxima = nota
    elif nota < minima:
        minima = nota
    if nota >= 5:
        aprobados += 1
    else:
        suspendidos += 1
    total += nota
print(f"Máxima: {maxima}")
print(f"Mínima: {minima}")
print(f"Media: {round(total/len(notas), 2)}")
print(f"Aprobados: {aprobados}")
print(f"Suspensos: {suspendidos}")
