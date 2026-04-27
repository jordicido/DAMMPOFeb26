'''
XXXXXXX
XX   XX
X X X X
X  X  X
X X X X
XX   XX
XXXXXXX
'''
altura = int(input("Introduce la altura del cuadrado (debe ser ipar): "))

print("X"*altura)
for i in range(1, altura-1):
    print("X", end="")
    for j in range(1, altura-1):
        if j == i or j == altura-1-i:
            print("X", end="")
        else:
            print(" ", end="")
    print("X")


print("X"*altura)