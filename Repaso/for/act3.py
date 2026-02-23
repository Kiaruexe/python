#Dado un conjunto de palabras, determina si hay alguna palabra que tenga más 
# de 10 caracteres. Si hay al menos una palabra que tenga más de 10 caracteres, 
# imprime la primera palabra encontrada que cumpla con este criterio. Si no hay 
# ninguna palabra que tenga más de 10 caracteres, imprime un mensaje indicando 
# que no se encontró ninguna palabra que cumpla con este criterio.

#Solicitamos al usuario la cantidad de palabras
num = int(input("Introduce la cantidad de palabras: "))
#Creamos una lista para almacenar las palabras
palabras = []
#Solicitamos al usuario que introduzca las palabras
for i in range(num):
    palabra = input(f"Introduce la palabra {i+1}: ")
    palabras.append(palabra)
#Buscamos una palabra con mas de 10 caracteres
for palabra in palabras:
    #Comprobamos si la palabra tiene mas de 10 caracteres
    if len(palabra) > 10:
        print(f"Se ha encontrado una palabra con mas de 10 caracteres: {palabra}")
        break
else:
    print("No se ha encontrado ninguna palabra con mas de 10 caracteres")