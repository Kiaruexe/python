#Implementar una función que calcule el promedio de una lista de números y 
# utilizar un decorador para validar que la lista no esté vacía antes de 
# calcular el promedio.
#Tareas:

#Definir una función promedio(lista) que calcule el promedio de una lista 
# de números. La función debe devolver el promedio como un valor de punto flotante.

#Definir un decorador validar_lista_no_vacia que tome como parámetro la 
# función promedio y valide que la lista de números no esté vacía antes de llamar 
# a la función promedio. Si la lista está vacía, el decorador debe lanzar 
# una excepción ValueError con el mensaje "La lista no puede estar vacía".

#Aplicar el decorador validar_lista_no_vacia a la función promedio usando 
# la notación @ y probar la función con diferentes listas de números.



#funcion validarListaNoVacia(func) que tome como parametro 
# la funcion promedio y valide que la lista de numeros no 
# este vacia antes de llamar a la funcion promedio. Si la 
# lista esta vacia, el decorador debe lanzar una excepcion 
# ValueError con el mensaje "La lista no puede estar vacia".
def validarListaNoVacia(func):
    def wrapper(lista):
        if not lista:
            raise ValueError("La lista no puede estar vacia")
        return func(lista)
    return wrapper

@validarListaNoVacia
def promedio(lista):
    return sum(lista) / len(lista)
try:
    print(promedio([1, 2, 3, 4, 5]))  
    print(promedio([])) 
except ValueError as e:
    print(e)