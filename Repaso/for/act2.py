#Dado un conjunto de nombres, determina si hay algún nombre que empiece
# con la letra "A". Si hay al menos un nombre que empiece con la letra "A", 
# imprime el primer nombre encontrado que cumpla con este criterio. Si no hay 
# ningún nombre que empiece con la letra "A", imprime un mensaje indicando que 
# no se encontró ningún nombre que cumpla con este criterio.

#Solicitamos al usuario la cantidad de nombres
num = int(input("Introduce la cantidad de nombres: "))
#Creamos una lista para almacenar los nombres
nombres = []
#Solicitamos al usuario que introduzca los nombres
for i in range(num):
    nombre = input(f"Introduce el nombre {i+1}: ")
    nombres.append(nombre)
#Buscamos un nombre que empiece con la letra A
for nombre in nombres:
    #Comprobamos si el nombre empieza con A
    if nombre.startswith("A") or nombre.startswith("a"):
        print(f"Se ha encontrado un nombre que empieza con A: {nombre}")
        break
else:
    print("No se ha encontrado ningun nombre que empiece con A")