#Ejercicio 4

#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M o los hombres con un nombre posterior 
# a la N y el grupo B por el resto.

#Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo (H o M): ")
sexo = sexo.upper()
if (sexo == "H" and nombre.lower() > "n") or (sexo == "M" and nombre.lower() < "m"):
    print("Perteneces al grupo A")
else:
    print("Perteneces al grupo B")