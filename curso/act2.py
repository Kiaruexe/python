#Algoritmo que pida un número y diga si es positivo, negativo o 0.

numero = float(input("Ingrese un numero: "))

if numero > 0:
    print("El numero es positivo")
elif numero == 0:
    print("El numero es 0")
else:
    print("El numero es negativo")