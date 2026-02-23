#7. Frecuencia mayor que K
#Extrae los elementos de la lista L cuya frecuencia es mayor que K. Siendo K un valor introducido por el usuario.
#L = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]

#Inicializamos la lista y pedimos el valor de K al usuario
L = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]
K = int(input("Introduce el valor de K: "))
frecuencias = {}
#Contamos la frecuencia de cada elemento en la lista
for numero in L:
    if numero in frecuencias:
        frecuencias[numero] += 1
    else:
        frecuencias[numero] = 1
resultado = []
#Extraemos los elementos cuya frecuencia es mayor que K
for numero, frecuencia in frecuencias.items():
    if frecuencia > K:
        resultado.append(numero)
print(f"Elementos con frecuencia mayor que {K}: {resultado}")
