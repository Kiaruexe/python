#Crea una función “calcularMaxMin” que recibe una lista con valores 
# numéricos y devuelve el valor máximo y el mínimo. Crea un programa que 
# pida números por teclado y muestre el máximo y el mínimo, utilizando 
# la función anterior.
def calcularMaxMin(lista):
    if not lista:
        return None, None
    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo
numeros = []
while True:
    entrada = input("Ingrese un numero (o 'fin' para terminar): ")
    if entrada.lower() == 'fin':
        break
    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Entrada erronea. Por favor, ingrese un numero valido.")
maximo, minimo = calcularMaxMin(numeros)
if maximo is not None and minimo is not None:
    print(f"El valor maximo es: {maximo}")
    print(f"El valor minimo es: {minimo}")
else:
    print("No se ingresaron numeros")