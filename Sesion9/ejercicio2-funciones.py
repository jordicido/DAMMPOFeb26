def saludo_personalizado(nombre, apellido, edad):
    return f"Hola {nombre} {apellido}, tienes {edad} años."
    
nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
edad = int(input("Introduce tu edad: "))
print(saludo_personalizado(nombre, apellido, edad))
