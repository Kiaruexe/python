#Dado un conjunto de números enteros, determina si hay algún número par en el conjunto. 
# Si hay al menos un número par, imprime el primer número par encontrado. Si no hay ningún 
# número par en el conjunto, imprime un mensaje indicando que no se encontró ningún número par.

#Solicitar al usuario la cantidad de numeros
num = int(input("Introduce la cantidad de numeros en el conjunto: "))
#Creamos una lista para almacenar los numeros
numeros = []
#Solicitamos al usuario que introduzca los numeros
for i in range(num):
    numero = int(input(f"Introduce el numero {i+1}: "))
    numeros.append(numero)
#Buscamos un numero par en la lista
for numero in numeros:
    #Comprobamos si el numero es par
    if numero % 2 == 0:
        print(f"Se ha encontrado un numero par: {numero}")
        break
else:
    print("No se ha encontrado ningun numero par en el conjunto")