#Ejercicio13
#Una imagen es un conjunto de pixeles distribuidos en forma de cuadrícula. 
# Cada pixel a su vez está conformado por otros componentes, que combinados 
# forman los colores que podemos ver en una imagen.
#RGB (Red Green Blue / Rojo Verde Azul), es uno de los espacios de color más 
# utilizado en cuanto a imágenes se trata. Posee 3 componentes y cada uno 
# toma valores de entre 0 y 255.
 
#Analizando la imagen anterior por ejemplo, para representar el color negro, 
# cada uno de los canales tiene valor de 0, mientras que para representar 
# el color blanco todos poseen 255.
#En este ejercicio se trata de que usando comprensión generes tuplas con 
# valores aleatorios para cada uno de los 3 canales.
#Crea una lista de listas (matriz) de distintos tamaños en la que cada celda 
# sea una tupla con de color RGB. El tamaño de la matriz vendrá determinado 
# por un valor que introduzca el usuario

#Puedes probar a crear matrices de:

#1- Matriz de 3x3
#2- Matriz de 3x10
#3- Matriz de 10x10
#4- Matriz de 28x28


import random

filas = int(input("Introduce el numero de filas: "))
columnas = int(input("Introduce el numero de columnas: "))

matriz_rgb = [
    [ (random.randint(0,255), random.randint(0,255), random.randint(0,255)) for _ in range(columnas) ]
    for _ in range(filas)
]

for fila in matriz_rgb:
    print(fila)
