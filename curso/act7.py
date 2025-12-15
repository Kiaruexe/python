#Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.
num = int(input("Ingrese un numero para ver su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {num}:")
for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")