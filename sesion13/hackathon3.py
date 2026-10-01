# control parental

edad = int(input("Edad: "))

if edad >= 18:
    print("ACCESO PERMITIDO")
elif edad >= 16:
    autorizacion = input("Autorización parental (s/n): ")
    if autorizacion.lower() == "s":
        print("ACCESO PERMITIDO")
    else:
        print("ACCESO DENEGADO")  
else:
    print("ACCESO DENEGADO")