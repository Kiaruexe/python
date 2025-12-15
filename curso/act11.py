#Escribe un programa que diga si un número introducido por teclado es o no 
# primo. Un número primo es aquel que sólo es divisible entre él mismo y la 
# unidad. Nota: Es suficiente probar hasta la raíz cuadrada del número para 
# ver si es divisible por algún otro número.

import math
num = int(input("Ingrese un numero para verificar si es primo: "))
esPrimo = True
if num < 2:
    esPrimo = False
else:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            esPrimo = False
            break

if esPrimo:
    print(f"El numero {num} es primo.")
else:
    print(f"El numero {num} no es primo.")
    