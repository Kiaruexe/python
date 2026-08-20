#Gestor de Biblioteca Personal

# Esta funcion pide al usuario una cantidad de libros y sus datos 
# y devuelve una lista de diccionarios con sus claves
def leerLibros():
    libros = []
    # Pedimos el numero de libros para introducir
    numLibros = int(input("Cuantos libros quieres introducir? "))
    for i in range(numLibros):
        print(f"\nIntroduciendo libro {i + 1}:")
        titulo = input("Titulo del libro: ")
        autor = input("Autor del libro: ")
        anio = int(input("Año de publicacion: "))
        # Convertimos la respuesta a mayusculas y comprobamos si es 'S'
        leido = input("Esta leido? (S/N): ").strip().upper() == 'S'

        # Construimos un diccionario por cada libro y lo añadimos a la lista
        libro = {
            'titulo': titulo,
            'autor': autor,
            'anio': anio,
            'leido': leido
        }
        libros.append(libro)
    return libros


# Esta funcion cuenta los libros leidos y los no leidos en la lista
def contarLibrosLeidos(libros):
    #Cuenta cuantos libros estan marcados como leidos y no leidos y devuelve una tupla
    
    # Sumamos 1 por cada libro cuyo valor 'leido' sea True
    leidos = sum(1 for libro in libros if libro['leido'])
    noLeidos = len(libros) - leidos
    return leidos, noLeidos


# Esta funcion calcula el año medio de publicacion de los libros
def calcularAnioMedio(libros):
    #Si la lista esta vacia devuelve None
    if not libros :
        return None
    totalAnio = sum(libro['anio'] for libro in libros)
    return totalAnio / len(libros)


# Esta funcion busca libros por un autor especifico en la lista
def buscarLibrosPorAutor(libros, autorBuscado):
    #Busca y devuelve libros cuyo autor coincida exactamente con el nombre
    return [libro for libro in libros if libro['autor'].lower() == autorBuscado.lower()]


# Esta funcion muestra un resumen de la biblioteca y los libros del autor buscado
def mostrarResumen(libros, autorBuscado):
    totalLibros = len(libros)
    leidos, noLeidos = contarLibrosLeidos(libros)
    anioMedio = calcularAnioMedio(libros)
    print("\n--- Resumen de la Biblioteca ---")
    print(f"Total de libros: {totalLibros}")
    print(f"Libros leidos: {leidos}")
    print(f"Libros no leidos: {noLeidos}")
    if anioMedio is not None:
        # Formateamos a 2 los decimales
        print(f"Año medio de publicacion: {anioMedio:.2f}")
    else:
        print("No hay libros para calcular el año medio de publicacion")
    # Buscamos los libros del autor solicitado e imprimimos titulo y año
    librosAutor = buscarLibrosPorAutor(libros, autorBuscado)
    if librosAutor:
        print(f"\nLibros del autor '{autorBuscado}':")
        for libro in librosAutor:
            print(f"- {libro['titulo']} ({libro['anio']})")
    else:
        print(f"\nNo hay libros del autor '{autorBuscado}'.")
            
# Programa principal
def main():
    libros = leerLibros()
    autorBuscado = input("\nIntroduce el nombre de un autor para buscar sus libros: ")
    mostrarResumen(libros, autorBuscado)


if __name__ == "__main__":
    main()