#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS 
# segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. 
# Escribir un algoritmo que determine la hora de llegada a la ciudad B.

def calcularHoraLlegada(horas, minutos, segundos, tiempoViaje):
    totalSegundos = horas * 3600 + minutos * 60 + segundos + tiempoViaje
    horasLlegada = (totalSegundos // 3600) % 24
    minutosLlegada = (totalSegundos % 3600) // 60
    segundosLlegada = totalSegundos % 60
    return horasLlegada, minutosLlegada, segundosLlegada
horas = int(input("Ingrese la hora de partida (HH): "))
minutos = int(input("Ingrese los minutos de partida (MM): "))
segundos = int(input("Ingrese los segundos de partida (SS): "))
tiempoViaje = int(input("Ingrese el tiempo de viaje en segundos (T): "))
horasLlegada, minutosLlegada, segundosLlegada = calcularHoraLlegada(horas, minutos, segundos, tiempoViaje)
print(f"La hora de llegada a la ciudad B es: {horasLlegada:02}:{minutosLlegada:02}:{segundosLlegada:02}")