"""
Script principal que importa el módulo areas y realiza varios cálculos de áreas.
"""

import areas


def main():
    # Área de un rectángulo de 5 x 9
    resultado = areas.area_rectangulo(5, 9)
    print(f"Área del rectángulo (5 x 9): {resultado}")

    # Área de un triángulo de base 5 y altura 13
    resultado = areas.area_triangulo(5, 13)
    print(f"Área del triángulo (base 5, altura 13): {resultado}")

    # Área de un círculo de radio 5
    resultado = areas.area_circulo(5)
    print(f"Área del círculo (radio 5): {resultado:.2f}")


if __name__ == "__main__":
    main()
