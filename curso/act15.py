#Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide 
# realizar un algoritmo que intercambie los valores de ambas variables y 
# muestre cuanto valen al final las dos variables.

def intercambiarValores(a, b):
    a, b = b, a
    return a, b
a = float(input("Ingrese el valor de A: "))
b = float(input("Ingrese el valor de B: "))
a, b = intercambiarValores(a, b)
print(f"El valor final de A es: {a}")
print(f"El valor final de B es: {b}")