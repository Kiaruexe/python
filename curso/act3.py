#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
import math

def calcularHipotenusa(cateto1, cateto2):
    hipotenusa = math.sqrt((cateto1*cateto1) + (cateto2*cateto2))
    return hipotenusa

cateto1 = float(input("Ingrese el primer cateto: "))
cateto2 = float(input("Ingrese el segundo cateto: "))
hipotenusa = calcularHipotenusa(cateto1, cateto2)
print(f"La hipotenusa del triangulo es: {hipotenusa:.2f}")