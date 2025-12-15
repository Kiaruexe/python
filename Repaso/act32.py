#Generar una lista de números primos hasta N.
#Escribe una función que devuelva una lista de números primos hasta un número
#dado utilizando el método de la Criba de Eratóstenes.

def cribaEratostenes(n):
    # Lista donde todos los numeros se consideran primos
    esPrimo = [True] * (n + 1)

    # El 0 y el 1 no son numeros primos
    esPrimo[0] = False
    esPrimo[1] = False

    # Recorremos los numeros desde 2 hasta n
    for i in range(2, n + 1):
        if esPrimo[i]:
            # Si es primo marcamos como no primos sus multiplos
            for j in range(i * 2, n + 1, i):
                esPrimo[j] = False

    primos = []

    # Recorremos la lista para encontrar los primos
    for i in range(n + 1):
        if esPrimo[i]:
            primos.append(i)
    return primos

n = int(input("Introduce un numero: "))
print("Numeros primos hasta", n, ":")
print(cribaEratostenes(n))
