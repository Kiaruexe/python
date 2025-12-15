#Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.
suma = 0
contador = 0
while True:
    num = int(input("Ingrese un numero (0 para terminar): "))
    if num == 0:
        break
    suma += num
    contador += 1
if contador > 0:
    media = suma / contador
    print(f"La suma de los numeros introducidos es: {suma}")
    print(f"La media de los numeros introducidos es: {media}")
else:
    print("No se introdujeron numeros")
