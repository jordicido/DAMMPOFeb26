# 10
'''
3
5
6
9
10
'''
numero = int(input("Introduce un número entero positivo\n"))

for i in range(numero+1):
    # Si el numero no es divisible entre 3 i tampoco entre 5 
    # o el numero es divisible entre 3 y 5 paso a la siguiente
    # iteracion
    if (i%3 != 0 and i%5 != 0) or (i%3 == 0 and i%5 == 0):
        continue
    
    print(i)
