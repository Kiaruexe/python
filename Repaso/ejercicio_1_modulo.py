"""
ejercicio_1_modulo.py
Módulo con funciones para generar, mostrar y ordenar una lista de números aleatorios.
"""

import random


def generar_lista():
    """
    Genera una lista de 7 números enteros aleatorios entre 0 y 100.

    Returns:
        list[int]: Lista con 7 números aleatorios.
    """
    return [random.randint(0, 100) for _ in range(7)]


def mostrar_lista(lista):
    """
    Muestra la lista por pantalla.

    Args:
        lista (list): Lista de números a mostrar.
    """
    print(f"  Lista: {lista}")


def ordenar_lista(lista):
    """
    Devuelve una nueva lista con los valores ordenados de menor a mayor.
    La lista original no se modifica.

    Args:
        lista (list): Lista de números a ordenar.

    Returns:
        list: Nueva lista ordenada.
    """
    return sorted(lista)
