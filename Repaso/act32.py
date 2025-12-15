def cribaEratostenes(n):
    esPrimo = [True] * (n + 1)
    esPrimo[0] = False
    esPrimo[1] = False

    for i in range(2, n + 1):
        if esPrimo[i]:
            for j in range(i * 2, n + 1, i):
                esPrimo[j] = False

    primos = []
    for i in range(n + 1):
        if esPrimo[i]:
            primos.append(i)

    return primos


n = int(input("Introduce un numero: "))
print("Numeros primos hasta", n, ":")
print(cribaEratostenes(n))
