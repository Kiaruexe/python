#Ejercicio 7 - Una Morsa con Mapa y Diccionario...
#En el siguiente ejercicio vamos a repasar el uso de maps, operador morsa (:=) y diccionarios.
#Dado el diccionario de datos dic:
#lista1 = [-3, -6, -9, -12, -15]
#Lista2 = [-18, 15, 12, 9, 6, 3]
#Lista3 = [2, 3, 4, 5, 6, 7, 8]
#dic = {1:lista1, 2:lista2, 3:lista3
#}

#La función funcionX recibe por parametro un valor(x) y devuelve un número decimal. 
# Las operaciones que realizan son las siguientes:
#Si x > 1:
#resultado = función exp(x)/x-1
#Si x < 1
#resultado = función exp(x)/(x-1)2
#Si x = 1:
#resultado = 0
#Implementa una función que aplique la función funcionX a todos los valores del diccionario 
# y se quede con aquellos resultados superiores a 0.5.

#a) El resultado debe aparecer en una única lista.
#b) El resultado aparezca dividido por cada lista del diccionario.
#Solución:

import math

lista1 = [-3, -6, -9, -12, -15]
lista2 = [-18, 15, 12, 9, 6, 3]
lista3 = [2, 3, 4, 5, 6, 7, 8]
dic = {1: lista1, 2: lista2, 3: lista3}

def funcionX(x):
    if x > 1:
        resultado = math.exp(x) / (x - 1)
    elif x < 1:
        resultado = math.exp(x) / ((x - 1) ** 2)
    else:
        resultado = 0
    return resultado

resultadoUnico = [
    resultado
    for lista in dic.values()
    for resultado in map(funcionX, lista)
    if (valor := resultado) > 0.5
]

print("Unico resultado: " )
print(resultadoUnico)

resultadoPorLista = {
    clave: [
        resultado
        for resultado in map(funcionX, lista)
        if (valor := resultado) > 0.5
    ]
    for clave, lista in dic.items()
}

print("Resultado por lista: " )
print(resultadoPorLista)