#Un alumno desea saber cual será su calificación final en la materia de Algoritmos.
# Dicha calificación se compone de los siguientes porcentajes:
# 55% del promedio de sus tres calificaciones parciales.
# 30% de la calificación del examen final.
# 15% de la calificación de un trabajo final.

def calcularCalificacionFinal(parcial1, parcial2, parcial3, examenFinal, trabajoFinal):
    promedioParciales = (parcial1 + parcial2 + parcial3) / 3
    calificacionFinal = (promedioParciales * 0.55) + (examenFinal * 0.3) + (trabajoFinal * 0.15)
    return calificacionFinal
parcial1 = float(input("Ingrese la primera calificacion parcial: "))
parcial2 = float(input("Ingrese la segunda calificacion parcial: "))
parcial3 = float(input("Ingrese la tercera calificacion parcial: "))
examenFinal = float(input("Ingrese la calificacion del examen final: "))
trabajoFinal = float(input("Ingrese la calificacion del trabajo final: "))
calificacionFinal = calcularCalificacionFinal(parcial1, parcial2, parcial3, examenFinal, trabajoFinal)
print(f"La calificacion final del alumno es: {calificacionFinal:.2f}")