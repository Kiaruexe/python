"""
Módulo que contiene funciones para calcular áreas de figuras geométricas.
"""

__author__ = "Alumno"
__version__ = "0.1"
__status__ = "Desarrollo"

import math


def area_rectangulo(base, altura):
    """Calcula y devuelve el área de un rectángulo."""
    return base * altura


def area_triangulo(base, altura):
    """Calcula y devuelve el área de un triángulo."""
    return (base * altura) / 2


def area_circulo(radio):
    """Calcula y devuelve el área de un círculo."""
    return math.pi * radio ** 2


if __name__ == "__main__":
    print("Ejecutando como programa principal")
    print(area_rectangulo(5, 9))
    print(area_triangulo(5, 13))
    print(area_circulo(5))
