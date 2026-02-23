#Ejercicio 4 - Divisores de X
#Crea un programa que pida al usuario un número comprendido entre el 
# 1 el 300 y genere una lista con todos los valores divisores.

#Resuelvelo sin y con comprensiones.

numero = int(input("Introduce un numero entre 1 y 300: "))
#sin comprensiones
divisores = []
for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)
print("Divisores sin comprensiones:", divisores)
#con comprensiones
divisoresComprension = [i for i in range(1, numero + 1) if numero % i == 0]
print("Divisores con comprensiones:", divisoresComprension)