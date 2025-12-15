#Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

nombre = input("Ingrese su nombre: ")
apellido1 = input("Ingrese su primer apellido: ")
apellido2 = input("Ingrese su segundo apellido: ")

iniciales = nombre[0].upper() + apellido1[0].upper() + apellido2[0].upper()
print(f"Las iniciales de la persona son: {iniciales}")