import random

def imprimir_carton(carton):
    print("---------      CARTÓN      ---------")
    for i in range(3):
        for j in range(5):
            print(carton[i][j], end="\t")
        print()

def comprobar_linea(carton):
    for i in range(3):
        if carton[i] == ["X", "X", "X", "X", "X"]:
            return True
    for j in range(5):
        if carton[0][j] == carton[1][j] == carton[2][j] == "X":
            return True
    return False

def comprobar_bingo(carton):
    return carton == [["X", "X", "X", "X", "X"],["X", "X", "X", "X", "X"],["X", "X", "X", "X", "X"]]


numeros_carton = random.sample(range(1,31),15) 
carton = []

for i in range(3):
    fila = []
    for j in range(5):
        fila.append(numeros_carton[i*5+j])
    carton.append(fila)

imprimir_carton(carton)

numeros_bingo = random.sample(range(1,31),30)
linea = False
intentos = 0

for i in range(len(numeros_bingo)):
    numero = numeros_bingo[i]
    print(f"Ha salido el numero {numero}")
    for i in range(3):
        for j in range(5):
            if carton[i][j] == numero:
                carton[i][j] = "X"
                break
    if not linea:
        linea = comprobar_linea(carton)
        if linea:
            print(f"Linea! Ha tardado {intentos} intentos")
    elif comprobar_bingo(carton):
        print(f"Bingo! Ha tardado {intentos} intentos")
        imprimir_carton(carton)
        break
    imprimir_carton(carton)
    input("Presiona Enter para sacar una bola...")
    intentos += 1