#Realizar un programa que compruebe si una cadena contiene una 
# subcadena. Las dos cadenas se introducen por teclado.
cadena = input("Ingrese una cadena de texto: ")
subcadena = input("Ingrese la subcadena para buscar: ")
if subcadena in cadena:
    print(f"La subcadena '{subcadena}' se encuentra en la cadena.")
else:
    print(f"La subcadena '{subcadena}' no se encuentra en la cadena.")