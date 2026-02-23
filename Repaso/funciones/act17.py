#Ejercicio 17. Juego del ahorcado.
#1- Numero de intentos del juego será 10.
#2- Tendremos una lista de palabras. Lo ideal seria cargar un fichero con todas las palabras del español, 
# pero por simplificar añadiremos 10 palabras a una lista.
#3- Cogeremos una de forma aletoria de esta lista de palabras. Una vez hecho, dará comienzo el juego del ahorcado. 
# Nota: investigar la forma de coger un elemento de forma aletoria de una lista de valores.
#4- Se nos irá pidiendo una letra en cada ronda, si acertamos se descubrirán las posiciones de la palabra que 
# contengan esa letra. Si fallamos se mantendrán ocultas con un * o un #.
#5- Tras introducir letra, el juego preguntará al jugador si quiere resolver, si la respuesta es Si, pedirá la 
# palabra al jugador. Podrán ocurrir 3 situaciones:
#El jugador acierta. La palabra introducida es correcta, el juego acaba con un mensaje de enhorabuena.
#No acierta. El juego continua.
#Ronda 10 y no se acierta. El jugador pierde automáticamente.

#importamos random para seleccionar una palabra aleatoria
import random
#Lista de palabras
palabras = ["Camarera", "Mesa", "Oficina", "Restaurante", "Profesora", "Móvil", "Cine", "Palomitas", "Sushi", "Gato"]
#Seleccionamos una palabra aleatoria y lo convertimos a mayusculas
palabraSecreta = random.choice(palabras).upper()
#Inicializamos a 10 los intentos
intentos = 10
#Conjunto para almacenar las letras adivinadas
letrasAdivinadas = set()
#Lista para mostrar la palabra con letras adivinadas y asteriscos
palabraMostrada = ['*' for i in palabraSecreta]
print("Juego del ahorcado")
#Bucle el cual dura especificamente 10 intentos
for intento in range(intentos):
    #Mostramos la palabra con las letras adivinadas y asteriscos
    print("\nPalabra: " + ''.join(palabraMostrada))
    #Pedimos una letra al usuario
    letra = input("Introduce una letra: ").upper()
    #Comprobamos si la letra ya ha sido adivinada
    if letra in letrasAdivinadas:
        print("Ya has adivinado esa letra, intenta con otra")
        continue
    #Comprobamos si la letra esta en la palabra secreta
    if letra in palabraSecreta:
        letrasAdivinadas.add(letra)
        #Actualizamos la palabra con la letra adivinada
        for i, char in enumerate(palabraSecreta):
            if char == letra:
                palabraMostrada[i] = letra
        if '*' not in palabraMostrada:
            print("\nHas adivinado la palabra: " + palabraSecreta)
            break
    else:
        print("Letra incorrecta.")
    #Preguntamos si quiere resolver o seguir intentando
    resolver = input("Quieres resolver la palabra? (S/N): ").upper()
    if resolver == 'S':
        intentoPalabra = input("Introduce la palabra: ").upper()
        if intentoPalabra == palabraSecreta:
            print("\nHas adivinado la palabra: " + palabraSecreta)
            break
        else:
            print("Palabra incorrecta.")
else:
    print("\nHas perdido, la palabra era: " + palabraSecreta)