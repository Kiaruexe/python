#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);
# si son iguales que lo indique.
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))

if num1 == num2 == num3:
    print("Los tres numeros son iguales.")
else:
    numeros = [num1, num2, num3]
    numeros.sort(reverse=True)
    print("Los numeros ordenados de mayor a menor son:", numeros)