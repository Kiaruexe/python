#Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 
# al 10) y posteriormente muestre en pantalla cada elemento de la lista junto 
# con su cuadrado y su cubo.
import random
listaNum = []
for i in range(1,11):
    listaNum.append(random.randint(1, 10))
for num in listaNum:
    print(f"Número: {num}, Cuadrado: {num**2}, Cubo: {num**3}")