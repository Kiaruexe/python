#Diseñar el algoritmo correspondiente a un programa, que:

#Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
#Carga la tabla con valores numéricos enteros.
#Suma todos los elementos de cada fila y todos los elementos de cada 
# columna visualizando los resultados en pantalla.
tabla = []
for i in range(6):
    fila = []
    for j in range(6):
        valor = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
        fila.append(valor)
    tabla.append(fila)
sumaFilas = [0] * 6
sumaColumnas = [0] * 6
for i in range(6):
    for j in range(6):
        sumaFilas[i] += tabla[i][j]
        sumaColumnas[j] += tabla[i][j]
for i in range(6):
    print(f"Suma de la fila {i}: {sumaFilas[i]}")
for j in range(6):
    print(f"Suma de la columna {j}: {sumaColumnas[j]}")