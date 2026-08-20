"""
Script principal que importa el módulo cadenas, solicita una cadena al usuario
y aplica todas las funciones disponibles.
"""

import cadenas


def main():
    texto = input("Introduce una cadena de texto: ")

    print(f"\nCadena invertida: {cadenas.invertir(texto)}")
    print(f"Número de vocales: {cadenas.contar_vocales(texto)}")
    print(f"En mayúsculas: {cadenas.a_mayusculas(texto)}")
    print(f"En minúsculas: {cadenas.a_minusculas(texto)}")


if __name__ == "__main__":
    main()
