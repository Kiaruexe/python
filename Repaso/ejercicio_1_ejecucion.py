"""
ejercicio_1_ejecucion.py
Programa principal que usa el módulo ejercicio_1_modulo para:
  1. Generar la lista
  2. Imprimir la lista
  3. Ordenar la lista
  4. Volver a imprimir la lista
"""

import ejercicio_1_modulo as modulo


print("=" * 40)
print("  EJERCICIO 1 - Módulos propios")
print("=" * 40)

# 1. Generar la lista
lista = modulo.generar_lista()
print("\n1. Lista generada:")
# 2. Imprimir la lista
modulo.mostrar_lista(lista)

# 3. Ordenar la lista
lista_ordenada = modulo.ordenar_lista(lista)
print("\n2. Lista después de ordenar:")
# 4. Volver a imprimir la lista
modulo.mostrar_lista(lista_ordenada)

print()
