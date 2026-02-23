#4. Valores.
#lista_numeros = [10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10]
#¿Sabrías hacer que Python te diga cuántas repeticiones del valor 10 hay en esta lista?

#Inicializamos la lista y el contador
listaNumeros = [10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10]
contador = 0
#Recorremos la lista y contamos las apariciones del numero 10
for numero in listaNumeros:
    if numero == 10:
        contador += 1
print(f"El numero 10 se repite {contador} veces en la lista")