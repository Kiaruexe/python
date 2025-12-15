#Pide una cadena y un carácter por teclado (valida que sea un carácter) y 
# muestra cuantas veces aparece el carácter en la cadena.
cadena = input("Ingrese una cadena de texto: ")
caracter = input("Ingrese un caracter para buscar en la cadena: ")
while len(caracter) != 1:
    print("Error: Debe ingresar un solo caracter.")
    caracter = input("Ingrese un caracter para buscar en la cadena: ")
contador = 0
for char in cadena:
    if char == caracter:
        contador += 1
print(f"El caracter '{caracter}' aparece {contador} veces en la cadena.")