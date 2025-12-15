#Crea un programa que pida dos número enteros al usuario y diga si alguno 
# de ellos es múltiplo del otro. Crea una función EsMultiplo que reciba los 
# dos números, y devuelve si el primero es múltiplo del segundo.
def EsMultiplo(num1, num2):
    if num2 == 0:
        return False
    return num1 % num2 == 0 or num2 % num1 == 0
num1 = int(input("Ingrese el primer numero entero: "))
num2 = int(input("Ingrese el segundo numero entero: "))
if EsMultiplo(num1, num2):
    print(f"Uno de los numeros {num1} y {num2} es multiplo del otro.")
else:
    print(f"Ninguno de los numeros {num1} y {num2} es multiplo del otro.")
    