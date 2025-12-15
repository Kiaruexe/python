#Queremos guardar los nombres y la edades de los alumnos de un curso. 
# Realiza un programa que introduzca el nombre y la edad de cada alumno. 
# El proceso de lectura de datos terminará cuando se introduzca como nombre 
# un asterisco (*) Al finalizar se mostrará los siguientes datos:

#Todos lo alumnos mayores de edad.
#Los alumnos mayores (los que tienen más edad)
alumnos = []
while True:
    nombre = input("Ingrese el nombre del alumno (o * para terminar): ")
    if nombre == "*":
        break
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    alumnos.append((nombre, edad))
mayoresDeEdad = [alumno for alumno in alumnos if alumno[1] >= 18]
if mayoresDeEdad:
    print("Alumnos mayores de edad:")
    for alumno in mayoresDeEdad:
        print(f"Nombre: {alumno[0]}, Edad: {alumno[1]}")
else:
    print("No hay alumnos mayores de edad")
    