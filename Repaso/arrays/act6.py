#Ejercicio 6 - Eliminando primera aparición
#Escribe un programa en python que elimine la primera aparición de un elemento 
# introducido por el usuario. Antes de eliminarlo comprueba si realmente existe en el array.

#array1 = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
#valor a eliminar = 3

#array2 = array('i', [1, 5, 3, 7, 1, 9, 3])
#valor a eliminar = 1

#array3 = array('i', [1, 5, 3, 7, 1, 9, 3])
#valor a eliminar = 8

from array import array

array1 = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
valorEliminar = int(input("Introduce el valor que quieres eliminar: "))
if valorEliminar in array1:
    array1.remove(valorEliminar)
    print(f"Valor {valorEliminar} eliminado, nuevo array: {array1}")
else:
    print(f"Valor {valorEliminar} no se pudo encontrar en el array")
    