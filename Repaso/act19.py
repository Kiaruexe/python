#Verificar si un número es perfecto.
#Implementa una función que determine si un número es perfecto (la suma de sus
#divisores propios es igual al número).

def esNumeroPerfecto(numero):
    sumaDivisores = 0

    # Recorremos los divisores propios
    for i in range(1, numero):
        if numero % i == 0:
            sumaDivisores += i

    # Comprobamos si la suma es igual al numero
    return sumaDivisores == numero


# Pedimos el numero por teclado
num = int(input("Introduce un numero: "))

if esNumeroPerfecto(num):
    print("El número es perfecto")
else:
    print("El número NO es perfecto")
