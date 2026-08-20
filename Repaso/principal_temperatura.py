"""
Script principal que importa el módulo temperatura, solicita una temperatura
en Celsius y muestra su conversión a Fahrenheit y Kelvin.
"""

import temperatura


def main():
    celsius = float(input("Introduce una temperatura en Celsius: "))

    fahrenheit = temperatura.celsius_a_fahrenheit(celsius)
    kelvin = temperatura.celsius_a_kelvin(celsius)

    print(f"\n{celsius} °C = {fahrenheit:.2f} °F")
    print(f"{celsius} °C = {kelvin:.2f} K")


if __name__ == "__main__":
    main()
