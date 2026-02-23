#Ejercicio 4.
#Dadas una cadena verifique si es pangrama o no.
#Una cadena es pangrama cuando contiene todas las letras del alfabeto.
#a) Desarrolla un algoritmo que nos diga si un texto es pangrama.
#Entrada:
#Un jugoso zumo de piña y kiwi bien frío es exquisito y no lleva alcohol.
#Resultado:
#True, la cadena es un pangrama

from string import ascii_lowercase as asc_lower

def esPangrama(cadena):
    # Convertimos la cadena a minusculas y creamos un conjunto de caracteres únicos
    caracteresUnicos = set(cadena.lower())
    # Verificamos si todas las letras del alfabeto estan en el conjunto
    for letra in asc_lower:
        if letra not in caracteresUnicos:
            return False
    return True
#Texto de ejemplo
texto = "Un jugoso zumo de piña y kiwi bien frio es exquisito y no lleva alcohol."
#Verificamos si el texto es un pangrama
if esPangrama(texto):
    print("True, la cadena es un pangrama")
else:
    print("False, la cadena no es un pangrama")