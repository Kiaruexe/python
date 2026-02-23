#Ejercicio 7. ¿Hay duplicados?
#Escribe un programa de Python para encontrar si un array de enteros contiene 
# algún elemento duplicado. Devuelve verdadero si algún valor aparece al menos 
# dos veces en dicha matriz y devuelve falso si cada elemento es distinto.

#Ejemplos de salida:

#array1 = array('i', [1, 5, 3, 7, 1, 9, 3])
#Verdadero

#array2 = array('i', [3, 7, 1, 9, 3])
#Verdadero

#array3 = array('i', [5, 3, 7, 1, 9])
#Falso

from array import array
array1 = array('i', [1, 5, 3, 7, 1, 9, 3])
array2 = array('i', [3, 7, 1, 9, 3])
array3 = array('i', [5, 3, 7, 1, 9])
def tieneDuplicados(arr):
    return len(set(arr)) != len(arr)
print(tieneDuplicados(array1))  
print(tieneDuplicados(array2))  
print(tieneDuplicados(array3)) 