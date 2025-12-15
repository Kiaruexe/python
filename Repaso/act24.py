def imprimirPascal(n):
    fila = [1]   # Primera fila

    for i in range(n):
        print(fila)

        nuevaFila = [1]  # Siempre empieza por 1

        for j in range(len(fila) - 1):
            suma = fila[j] + fila[j + 1]
            nuevaFila.append(suma)

        nuevaFila.append(1)  # Siempre termina en 1
        fila = nuevaFila

# Programa principal
n = int(input("Introduce el numero de filas: "))
imprimirPascal(n)