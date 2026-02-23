#Ejercicio 7 - Los números Glotones
#Implementar un programa que primero muestre en pantalla los números del 1 al 100, 
# a continuación mostrará de nuevo la misma lista de números pero sustituyendo los 
# múltiplos de 3 por el palabra "ÑAM" y, a su vez, los múltiplos de 5 por "A_COMER". 
# Para los números que, al mismo tiempo, son múltiplos de 3 y 5, mostrar el mensaje "ÑAM_ÑAM_A_COMER".

#Soluciona el problema con y sin comprensiones.

#sin comprensiones
numeros = list(range(1, 101))
print("Números del 1 al 100:", numeros)
resultado = []
for numero in numeros:
    if numero % 3 == 0 and numero % 5 == 0:
        resultado.append("ÑAM_ÑAM_A_COMER")
    elif numero % 3 == 0:
        resultado.append("ÑAM")
    elif numero % 5 == 0:
        resultado.append("A_COMER")
    else:
        resultado.append(numero)
print("Resultado sin comprensiones:", resultado)
#con comprensiones
resultadoComprension = ["ÑAM_ÑAM_A_COMER" if numero % 3 == 0 and numero % 5 == 0 else "ÑAM" 
                        if numero % 3 == 0 else "A_COMER" if numero % 5 == 0 else numero for numero in numeros]
print("Resultado con comprensiones:", resultadoComprension)