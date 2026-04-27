altura = int(input("Introduce la altura del triángulo\n"))

for i in range(1, altura+1, 1):
    for j in range(0, i): 
        print("*", end="")
    print()
