#Ejercicio 5.
#Se nos dan una lista con n listas (matriz de listas) de cualquier 
# tamaño que pueden tener elementos comunes.
#Necesitamos combinar todas estas matrices de tal manera que cada 
# elemento deba aparecer solo una vez y los elementos deben estar ordenados.
#Entrada:
#matriz = [
#[1, 2, 2, 4, 3, 6],
#[5, 1, 3, 4],
#[9, 5, 7, 1],
#[2, 4, 1, 3]
#]
#Salida:
#[1, 2, 3, 4, 5, 6, 7, 9]

matriz = [
    [1, 2, 2, 4, 3, 6],
    [5, 1, 3, 4],
    [9, 5, 7, 1],
    [2, 4, 1, 3]
]
# Usamos un conjunto para almacenar los elementos unicos
elementosUnicos = set()
# Recorremos cada sublista en la matriz
for sublista in matriz:
    # Añadimos cada elemento de la sublista al conjunto
    for elemento in sublista:
        elementosUnicos.add(elemento)
# Convertimos el conjunto a una lista y la ordenamos
resultado = sorted(list(elementosUnicos))
print(f"Elementos únicos ordenados: {resultado}")