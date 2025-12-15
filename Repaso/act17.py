def esPalindromo(cadena):
    # Convertimos a minusculas y eliminamos espacios
    texto = cadena.lower().replace(" ", "")
    
    # Comprobamos si es igual al derecho y al reves
    return texto == texto[::-1]


# Pedimos la cadena por teclado
cadena = input("Introduce una cadena de texto: ")

if esPalindromo(cadena):
    print("La cadena es un palindromo")
else:
    print("La cadena NO es un palindromo")
