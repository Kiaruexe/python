"""
Módulo que contiene funciones para la manipulación de cadenas de texto.
"""

__author__ = "Alumno"
__version__ = "0.1"
__status__ = "Desarrollo"


def invertir(cadena):
    """Devuelve la cadena invertida."""
    return cadena[::-1]


def contar_vocales(cadena):
    """Cuenta y devuelve el número de vocales en la cadena."""
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    contador = 0
    for letra in cadena:
        if letra in vocales:
            contador += 1
    return contador


def a_mayusculas(cadena):
    """Convierte la cadena a mayúsculas."""
    return cadena.upper()


def a_minusculas(cadena):
    """Convierte la cadena a minúsculas."""
    return cadena.lower()


if __name__ == "__main__":
    print("Ejecutando como programa principal")
    texto = "Hola Mundo"
    print(invertir(texto))
    print(contar_vocales(texto))
    print(a_mayusculas(texto))
    print(a_minusculas(texto))
