#Realizar un programa que comprueba si una cadena leída por teclado 
# comienza por una subcadena introducida por teclado.
cadena = input("Ingrese una cadena de texto: ")
subcadena = input("Ingrese la subcadena para verificar el inicio: ")
if cadena.startswith(subcadena):
    print(f"La cadena comienza con la subcadena '{subcadena}'.")
else:
    print(f"La cadena no comienza con la subcadena '{subcadena}'.")