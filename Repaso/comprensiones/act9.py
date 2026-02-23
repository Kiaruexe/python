#Ejercicio 9
#Dada la siguiente estructura de datos:

#alumnos = [{"Pedro":[5,7,9]},{"Sergio":[3,3,3]},{"Ibtihal":[5,5,5]},{"Angel":[7,7,9]},{"Fede":[5,5,7]}, {"Mik": [7,5,10]}]

#Devuelve el nombre y la nota media con 1 decimal de los alumnos cuya 
# nombre tiene 4 letras o más y su nota media es superior a 6.

#a) Implementa el algoritmo utilizando bucles de la manera habitual.
#b) Soluciona el problema utilizando comprension de listas

alumnos = [{"Pedro":[5,7,9]},{"Sergio":[3,3,3]},{"Ibtihal":[5,5,5]},{"Angel":[7,7,9]},{"Fede":[5,5,7]}, {"Mik": [7,5,10]}]
# a) Solución con bucles
resultados = []
for alumno in alumnos:
    for nombre, notas in alumno.items():
        media = sum(notas) / len(notas)
        if len(nombre) >= 4 and media > 6:
            resultados.append((nombre, round(media, 1)))
print("Resultados con bucles:", resultados)
# b) Solución con comprensión de listas
resultadosComprension = [(nombre, round(sum(notas) / len(notas), 1)) 
                        for alumno in alumnos 
                        for nombre, notas in alumno.items() 
                        if len(nombre) >= 4 and (sum(notas) / len(notas)) > 6]
print("Resultados con comprensión de listas:", resultadosComprension)