#Imprimir las primeras N filas de Pascal.
#Crea una función que imprima las primeras N filas del Triángulo de Pascal.

def imprimirPascal(n):
    # La primera fila del triángulo siempre es [1]
    fila = [1]
    # Bucle que se repite n veces 
    for i in range(n):
        print(fila)
        #fila que siempre empieza por 1
        nuevaFila = [1]
        # Bucle para sumar los numeros de la fila anterior
        for j in range(len(fila) - 1):
            # Se suman dos numeros consecutivos
            suma = fila[j] + fila[j + 1]
            # Se añade la suma a la nueva fila
            nuevaFila.append(suma) 
        # La nueva fila siempre termina en 1
        nuevaFila.append(1)
        # Actualizamos la fila para la siguiente vuelta
        fila = nuevaFila
        
n = int(input("Introduce el numero de filas: "))
# Llamamos a la funcion para mostrar el triangulo
imprimirPascal(n)
