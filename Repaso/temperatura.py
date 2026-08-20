"""
Módulo que contiene funciones para la conversión entre distintas escalas de temperatura.
"""

__author__ = "Alumno"
__version__ = "0.1"
__status__ = "Desarrollo"


def celsius_a_fahrenheit(c):
    """Convierte grados Celsius a Fahrenheit."""
    return (c * 9 / 5) + 32


def celsius_a_kelvin(c):
    """Convierte grados Celsius a Kelvin."""
    return c + 273.15


def fahrenheit_a_celsius(f):
    """Convierte grados Fahrenheit a Celsius."""
    return (f - 32) * 5 / 9


def kelvin_a_celsius(k):
    """Convierte Kelvin a Celsius."""
    return k - 273.15


if __name__ == "__main__":
    print("Ejecutando como programa principal")
    print(celsius_a_fahrenheit(100))
    print(celsius_a_kelvin(100))
    print(fahrenheit_a_celsius(212))
    print(kelvin_a_celsius(373.15))
