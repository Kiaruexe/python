#4- Escribir un programa que pida al usuario que introduzca una frase en la consola y 2 vocales, 
# y después muestre por pantalla la misma frase pero con las vocales introducidas en mayúsculas.

frase = input("Introduzca una frase: ")
vocal1 = input("Introduzca la primera vocal: ")
vocal2 = input("Introduzca la segunda vocal: ")

frase = frase.replace(vocal1, vocal1.upper())
frase = frase.replace(vocal2, vocal2.upper())

print(frase)