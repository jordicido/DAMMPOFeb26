# Operadores aritméticos
# +, -, *, /, //, **, %

num1 = 10
num2 = 20

print(f"num1 + num2 = {num1+num2}") # 30
print(f"num1 - num2 = {num1-num2}") # -10
print(f"num1 * num2 = {num1*num2}") # 200
print(f"num1 / num2 = {num1/num2}") # 0.5
print(f"num1 // num2 = {num1//num2}") # 0
print(f"num1 ** nm2 = {num1**num2}") # 10²⁰
print(f"num1 % num2 = {num2%num1}") # 10

# Operadores comparación 
# ==, !=, >, >=, <, <=

a = 12
b = 6

print(f"Son iguales? {a == b}") # False
print(f"Son diferentes? {a != b}") # True
print(f"a es mayor que b? {a > b}") # True
print(f"a es menor que b? {a < b}") # False
print(f"a es mayor o igual que b? {a >= b}") # True
print(f"a es menor o igual que b? {a <= b}") # False

# Operadores lógicos
# and, or, not

carnet = True
edad = 37
invitacion = True
alumno = False

print(f"puedo conducir si tengo carnet y soy mayor de edad: {carnet and edad >= 18}")
print(f"puedo entrar a la reunion de meet? {invitacion or alumno}")
print(f"Soy mayor de edad si {not edad < 18}")

# Asignación compuesta

numero = 1
numero = numero + a
numero = numero + 1 #2
numero = numero + 1 #3
numero += a
numero -= 1
numero /= 1
numero *= 1



