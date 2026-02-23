#9. Números consecutivos.
#Diseña un programa que muestre aquellos números que se encuentran repetidos exactamente 3 veces.
#Ejemplos:
#Entrada: [4, 5, 5, 5, 3, 8]
#Salida: 5
#Entrada: [1, 1, 1, 64, 23, 64, 22, 22, 22]
#Salida : 1, 22

#Inicializamos la lista y el contador
numeros = [4, 5, 5, 5, 3, 3, 3, 3, 8, 1, 1, 1, 64, 23, 64, 22, 22, 22]
contador = {}
#Contamos las apariciones de cada numero
for numero in numeros:
    if numero in contador:
        contador[numero] += 1
    else:
        contador[numero] = 1
#Mostramos los numeros que se repiten exactamente 3 veces
for numero, veces in contador.items():
    if veces == 3:
        print(f"Numero {numero} se repite exactamente 3 veces")