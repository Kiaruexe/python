#Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5
for n in range(1, 6):
    print(f"\nTabla de multiplicar del {n}:")
    for i in range(1, 11):
        resultado = n * i
        print(f"{n} x {i} = {resultado}")