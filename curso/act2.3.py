#Escribe un programa que lea una cadena y devuelva un diccionario 
# con la cantidad de apariciones de cada carácter en la cadena.
cadena = input("Ingrese una cadena de texto: ")
contadorCaracteres = {}
for caracter in cadena:
    if caracter in contadorCaracteres:
        contadorCaracteres[caracter] += 1
    else:
        contadorCaracteres[caracter] = 1
for caracter, cantidad in contadorCaracteres.items():
    print(f"El caracter '{caracter}' aparece {cantidad} veces en la cadena.")