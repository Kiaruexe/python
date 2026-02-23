#Ejercicio 7
#Nos han encargado que diseñemos un programa para detectar bombas de una lista de N números.
#Serán bombas todos los números que contengan el número que introduzca el jefe de los TEDAX por teclado(0-9)
#lista_con_bombas=[11, 107, 17, 67, 99, 45, 37, 87, 1007, 2007, 2027, 10007, 7, 1, 15, 81, 91, 88, 307]
#a) Analiza la lista para indicar el jefe TEDAX si hay bomba o la lista es segura.
#b) Modifica el programa para en caso de existir bombas, indicar el nº y la posición en la que se encuentra de la lista de bombas

#Creamos la lista con bombas
listaConBombas=[11, 107, 17, 67, 99, 45, 37, 87, 1007, 2007, 2027, 10007, 7, 1, 15, 81, 91, 88, 307]
#Solicitamos al usuario el numero de bomba
numBomba=input("Introduce el numero de bomba: ")
#Variable para controlar si hay bomba inicializada en False
hayBomba=False
#Recorremos la lista para buscar bombas
for i in range(len(listaConBombas)):
    #Comprobamos si el numero de bomba esta en el numero de la lista
    if numBomba in str(listaConBombas[i]):
        print(f"Bomba encontrada: {listaConBombas[i]} en la posicion {i}")
        hayBomba=True
    break
else:
    print("La lista es segura, no se han encontrado bombas")