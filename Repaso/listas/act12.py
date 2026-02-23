#12. Conservar Registros con N Apariciones del valor K
#Queremos conservar aquellos registros cuyo valor K esté N veces.
#Entrada :
#lista_prueba = [[4, 5, 5, 4],[5, 4, 3]]
#K = 5
#N = 2
#Salida :
#[[4, 5, 5, 4]]
#Entrada :
#lista_prueba = [[4, 5, 5, 4],[5, 4, 3]]
#K = 5
#N = 3
#Salida :
#[]

#Inicializamos la lista, pedimos K y N al usuario
listaPrueba = [[4, 5, 5, 4],[5, 4, 3]]
K = int(input("Introduce el valor de K: "))
N = int(input("Introduce el valor de N: "))
resultado = []
#Revisamos cada sublista y comprobamos si K aparece N veces
for sublista in listaPrueba:
    if sublista.count(K) == N:
        resultado.append(sublista)
print(f"Listas que contienen el valor {K} exactamente {N} veces: {resultado}")
