def esNumeroPerfecto(numero):
    sumaDivisores = 0

    # Recorremos los divisores propios
    for i in range(1, numero):
        if numero % i == 0:
            sumaDivisores += i

    # Comprobamos si la suma es igual al número
    return sumaDivisores == numero


# Pedimos el número por teclado
num = int(input("Introduce un numero: "))

if esNumeroPerfecto(num):
    print("El número es perfecto")
else:
    print("El número NO es perfecto")
