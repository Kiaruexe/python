#Suponiendo que hemos introducido una cadena por teclado que representa 
# una frase (palabras separadas por espacios), realiza un programa que 
# cuente cuantas palabras tiene.
frase = input("Ingrese una frase: ")
palabras = frase.split()
cantidadPalabras = len(palabras)
print(f"La frase tiene {cantidadPalabras} palabras.")