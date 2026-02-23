#10. Transforma los siguientes códigos a comprensiones de lista.
#Desempaqueta todos los números de la matriz 3D en una única lista
#Desempaqueta todos los nombres de la matriz 2D para que estén todos 
# capitalizados (primera letra en mayúsculas)
#Obten una lista solo con las letras que están en mayusculas.
#Te dejo una imagen en la que se resuelven los 3 puntos sin comprensiones, 
# tu misión es modificarlos para que hagan lo mismo pero empleando comprensiones.

matriz = [[[1, 2], [3, 4]], [[5]]]
desempaquetado = [ele for elementos in matriz for elemento in elementos for ele in elemento]
print(desempaquetado)

grupoNombres = ['Vahee', 'ADam', ['Dylan', 'DiANa']]
capitalizados = [nombre.capitalize() for nombres in grupoNombres for nombre 
                 in (nombres if isinstance(nombres, list) else [nombres])]
print(capitalizados)

letras = "ABcdefghIjKLmnÑOpQrStUvWXYZ"
mayus = [letra for letra in letras if letra.isupper()]
print(mayus)

