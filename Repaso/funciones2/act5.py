#Ejercicio 5. 🐌 El ascenso del Caracol🐌
#Un caracol que asciende por una pared de 125 cm. Cada día recorre una distancia 
# aleatoria de centímetros. Durante la noche, al quedarse dormido, desciende 20 centímetros.

#Diseña una función que nos devuelva en cuantos días el caracol llega al final de la pared.

#DATOS:
#La distancia que recorre cada día viene en la siguiente lista:
#distancias_diarias = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]. Cada día recorre una de 
# las cifras empezando por la izquierda.
#Altura_muro = 125. Es la altura del muro
#caida_nocturna = 20 Son los centimetros que desciende durante la noche
#total_distancia_recorrida = 0 Distancia total recorrida por el caracol

distanciasDiarias = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
alturaMuro = 125
caidaNocturna = 20
totalDistanciaRecorrida = 0
dias = 0

def ascensoCaracol():
    global totalDistanciaRecorrida, dias
    for distancia in distanciasDiarias:
        totalDistanciaRecorrida += distancia
        dias += 1
        if totalDistanciaRecorrida >= alturaMuro:
            break
        totalDistanciaRecorrida -= caidaNocturna
    return dias

diasNecesarios = ascensoCaracol()
print(f"El caracol necesita {diasNecesarios} dias")