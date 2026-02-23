#Ejercicio 2 - El buscador de Aes.
#Dada una frase cualquiera, transforma cada palabra aplicando el siguiente criterio:
#Si la palabra contiene al menos una a la ponemos en mayuscula.
#Si la palabra NO contiene ninguna a irá con formato de título.

#a) Resuelve el problema sin comprensiones.
#b) Soluciona el ejercicio usando comprensión.

frase = input("Introduce una frase: ")
#sin comprensiones
palabras = frase.split()
resultado = []
for palabra in palabras:
    if 'a' in palabra.lower():
        resultado.append(palabra.upper())
    else:
        resultado.append(palabra.title())
print("Resultado sin comprensiones:", " ".join(resultado))
#con comprensiones
resultadoComprension = [palabra.upper() if 'a' in palabra.lower() else palabra.title() for palabra in frase.split()]
print("Resultado con comprensiones:", " ".join(resultadoComprension))