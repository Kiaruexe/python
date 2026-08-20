"""
paquete/ejercicio_2_modulo.py
Módulo con la lógica del programa 'Las bolas del descuento'.
"""

import random

# Tabla de descuentos: color -> porcentaje (0 = sin descuento)
BOLAS = {
    "BLANCA":   0,
    "ROJA":    10,
    "AZUL":    20,
    "VERDE":   25,
    "AMARILLA": 50,
}

MINIMO_COMPRA = 100.0


def pedir_compra():
    """
    Solicita al usuario el importe total de sus compras.

    Returns:
        float: Importe introducido por el usuario.
    """
    while True:
        try:
            importe = float(input("  Introduce el total de tu compra (€): ").replace(",", "."))
            if importe < 0:
                print("  El importe no puede ser negativo. Inténtalo de nuevo.")
            else:
                return importe
        except ValueError:
            print("  Valor no válido. Introduce un número.")


def seleccionar_bola():
    """
    Selecciona aleatoriamente una bola de la lista de colores disponibles.

    Returns:
        str: Nombre del color de la bola seleccionada.
    """
    return random.choice(list(BOLAS.keys()))


def calcular_descuento(importe, bola):
    """
    Calcula el descuento y el importe final según la bola seleccionada.

    Args:
        importe (float): Importe total de la compra.
        bola (str):      Color de la bola seleccionada.

    Returns:
        tuple[int, float]: (porcentaje_descuento, importe_final)
    """
    porcentaje = BOLAS[bola]
    importe_final = importe * (1 - porcentaje / 100)
    return porcentaje, round(importe_final, 2)


def mostrar_resultado(importe, bola, porcentaje, importe_final):
    """
    Muestra por pantalla el resultado del sorteo y el importe a pagar.

    Args:
        importe (float):       Importe original de la compra.
        bola (str):            Color de la bola seleccionada.
        porcentaje (int):      Porcentaje de descuento aplicado.
        importe_final (float): Importe a pagar tras el descuento.
    """
    print(f"\n  🎱 ¡Ha salido la bola {bola}!")
    if porcentaje == 0:
        print("  Lo sentimos, la bola blanca no tiene descuento.")
        print(f"  Total a pagar: {importe:.2f} €")
    else:
        print(f"  ¡Enhorabuena! Tienes un descuento del {porcentaje}%.")
        print(f"  Importe original : {importe:.2f} €")
        print(f"  Descuento        : -{importe - importe_final:.2f} €")
        print(f"  Total a pagar    : {importe_final:.2f} €")


def ejecutar_promocion():
    """
    Función principal del módulo. Gestiona todo el flujo del programa.
    """
    print("\n" + "=" * 45)
    print("    🛒  LAS BOLAS DEL DESCUENTO  🛒")
    print("=" * 45)

    importe = pedir_compra()

    if importe < MINIMO_COMPRA:
        print(f"\n  Tu compra es de {importe:.2f} €.")
        print(f"  No se aplica ninguna promoción (mínimo {MINIMO_COMPRA:.2f} €).")
    else:
        bola = seleccionar_bola()
        porcentaje, importe_final = calcular_descuento(importe, bola)
        mostrar_resultado(importe, bola, porcentaje, importe_final)

    print("=" * 45 + "\n")
