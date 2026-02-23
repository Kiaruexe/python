#5. Números Amigos
#Se dice que dos números son amigos si la suma de los divisores del primero de los números 
# es igual a al segundo nº y la suma de divisores del segundo número es igual al primero.
#Desarrolla un programa que nos permita saber si dos números son amigos.
#Implementa una versión avanzada de tu programa para que te permita calcular los N primeros pares amigos.

#Función para calcular la suma de los divisores
def sumaDivisores(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma
#Funcion para comprobar si dos numeros son amigos
def sonAmigos(num1, num2):
    return sumaDivisores(num1) == num2 and sumaDivisores(num2) == num1
#Pedimos dos numeros al usuario
numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))
#Comprobamos si son amigos
if sonAmigos(numero1, numero2):
    print(f"{numero1} y {numero2} son numeros amigos")
else:
    print(f"{numero1} y {numero2} no son numeros amigos")
#Versión avanzada para encontrar los N primeros pares amigos
N = int(input("Introduce cuantos pares amigos quieres encontrar: "))
#Inicializamos variables
encontrados = 0
num = 1
paresAmigos = []
#Bucle hasta encontrar N pares amigos
while encontrados < N:
    amigo = sumaDivisores(num)
    if amigo != num and sonAmigos(num, amigo):
        # Evitamos duplicados
        if (amigo, num) not in paresAmigos:  
            paresAmigos.append((num, amigo))
            encontrados += 1
    num += 1
#Mostramos los pares amigos encontrados (si le ponemos un numero alto en n tarda en mostrar la respuesta)
print(f"Los primeros {N} pares de numeros amigos son:")
for par in paresAmigos:
    print(par)
    