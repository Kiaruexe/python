#3 Lanzamiento de 100mil dados de 6 caras
#Usar una lista de comprensión para dibujar muchos números aleatorios
#Usar sum y una expresión generadora para contar valores.
#Convierte el siguiente código a una versión sin comprensiones.
#!!Lancemos un dado 100 mil veces!!

import random as rd

numeros = []
for i in range(100000):
    numero = rd.randint(1, 6)
    numeros.append(numero)

contador6 = 0
for num in numeros:
    if num == 6:
        contador6 += 1

probabilidad6 = (contador6 / 100000) * 100

print(f"La probabilidad de sacar un 6 es de: {probabilidad6}")
