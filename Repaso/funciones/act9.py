#Ejercicio 9
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo 
# como el de más abajo, de altura el número introducido.


#Tenemos que hacer dos bucles:
#1- Bucle para el nº de filas
#2- Bucle para el nº de asteriscos por fila.


num = int(input("Introduce un numero: "))
for i in range(num):
    for j in range(i+1):
        print("*", end="")
    print("")