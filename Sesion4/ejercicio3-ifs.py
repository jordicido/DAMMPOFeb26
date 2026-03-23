pacman = int(input("Dime la posición de Pacman\n"))
fantasma = int(input("Dime la posición del fantasma\n"))

if pacman == fantasma:
    estado = input("Dime el estado de Pacman(normal/caramelo)\n")
    if estado == "normal":
        print("Pacman ha sido atrapado")
    elif estado == "caramelo": 
        print("Pacman ha comido fantasma")
else:
    print("Pacman ha escapado")