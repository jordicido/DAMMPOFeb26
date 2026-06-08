frase = input("Ingresa la frase en minúscula y sin puntuación: ").split()
frecuencia_palabras = {}

for palabra in frase:
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1

print(frecuencia_palabras)