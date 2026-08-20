"""
Ejercicio 1 - Cifrado Vigenere
Cifra o descifra un mensaje usando el algoritmo de Vigenere con un alfabeto
de 27 letras (español, incluye la Ñ).

Uso:
    Cifrar:    python cifrado_vigenere.py -c PROGRAMACIONDEIA -k covid
    Descifrar: python cifrado_vigenere.py -d RGKÑUCAVKLQBYMLC -k covid
"""

import sys

# Alfabeto español de 27 letras (posiciones 0-26)
ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
TOTAL = len(ALFABETO)  # 27


def letra_a_pos(letra):
    """Devuelve la posición (0-26) de una letra en el alfabeto."""
    return ALFABETO.index(letra)


def pos_a_letra(pos):
    """Devuelve la letra correspondiente a una posición (0-26)."""
    return ALFABETO[pos]


def cifrar(mensaje, clave):
    """
    Cifra el mensaje usando la clave con el algoritmo de Vigenere.

    Args:
        mensaje (str): Texto a cifrar (solo letras mayúsculas del alfabeto).
        clave (str):   Palabra clave en mayúsculas.

    Returns:
        str: Mensaje cifrado.
    """
    resultado = []
    n_clave = len(clave)

    for i, letra_msg in enumerate(mensaje):
        letra_clave = clave[i % n_clave]
        pos_cifrada = (letra_a_pos(letra_msg) + letra_a_pos(letra_clave)) % TOTAL
        resultado.append(pos_a_letra(pos_cifrada))

    return "".join(resultado)


def descifrar(mensaje, clave):
    """
    Descifra el mensaje usando la clave con el algoritmo de Vigenere.

    Args:
        mensaje (str): Texto cifrado (solo letras mayúsculas del alfabeto).
        clave (str):   Palabra clave en mayúsculas.

    Returns:
        str: Mensaje descifrado.
    """
    resultado = []
    n_clave = len(clave)

    for i, letra_msg in enumerate(mensaje):
        letra_clave = clave[i % n_clave]
        pos_descifrada = (letra_a_pos(letra_msg) - letra_a_pos(letra_clave)) % TOTAL
        resultado.append(pos_a_letra(pos_descifrada))

    return "".join(resultado)


def validar_texto(texto, contexto="mensaje"):
    """
    Comprueba que todas las letras del texto pertenecen al alfabeto.

    Args:
        texto (str):    Texto a validar (ya en mayúsculas).
        contexto (str): Nombre descriptivo para el mensaje de error.

    Raises:
        ValueError: Si algún carácter no pertenece al alfabeto.
    """
    for c in texto:
        if c not in ALFABETO:
            raise ValueError(
                f"El carácter '{c}' en el {contexto} no pertenece al alfabeto.\n"
                f"Usa solo las letras: {ALFABETO}"
            )


def mostrar_tabla(mensaje, clave, resultado, modo):
    """Muestra la tabla de enfrentamiento letra a letra."""
    n_clave = len(clave)
    clave_extendida = "".join(clave[i % n_clave] for i in range(len(mensaje)))
    operador = "+" if modo == "cifrar" else "-"

    print(f"\n{'─'*55}")
    print(f"  {'Mensaje':>12} : {mensaje}")
    print(f"  {'Clave':>12} : {clave_extendida}")
    print(f"  {'Operación':>12} : posición(msg) {operador} posición(clave)  mod {TOTAL}")
    print(f"{'─'*55}")

    for i, (lm, lc, lr) in enumerate(zip(mensaje, clave_extendida, resultado)):
        pm = letra_a_pos(lm)
        pc = letra_a_pos(lc)
        pr = letra_a_pos(lr)
        if modo == "cifrar":
            detalle = f"({pm:2d} + {pc:2d}) % {TOTAL} = {pr:2d}"
        else:
            detalle = f"({pm:2d} - {pc:2d}) % {TOTAL} = {pr:2d}"
        print(f"  {lm} {operador} {lc}  =>  {detalle}  =>  {lr}")

    print(f"{'─'*55}")
    accion = "Cifrado" if modo == "cifrar" else "Descifrado"
    print(f"  {accion}: {resultado}\n")


def parsear_argumentos(args):
    """
    Parsea los argumentos de la línea de comandos.

    Returns:
        tuple: (modo, texto, clave)  donde modo es 'cifrar' o 'descifrar'.

    Raises:
        SystemExit: Si los argumentos son incorrectos.
    """
    modo   = None
    texto  = None
    clave  = None

    i = 0
    while i < len(args):
        if args[i] == "-c":
            if modo == "descifrar":
                print("Error: No se puede cifrar y descifrar a la vez.")
                sys.exit(1)
            modo = "cifrar"
            i += 1
            if i >= len(args):
                print("Error: Falta el texto después de -c.")
                sys.exit(1)
            texto = args[i].upper()
        elif args[i] == "-d":
            if modo == "cifrar":
                print("Error: No se puede cifrar y descifrar a la vez.")
                sys.exit(1)
            modo = "descifrar"
            i += 1
            if i >= len(args):
                print("Error: Falta el texto después de -d.")
                sys.exit(1)
            texto = args[i].upper()
        elif args[i] == "-k":
            i += 1
            if i >= len(args):
                print("Error: Falta la clave después de -k.")
                sys.exit(1)
            clave = args[i].upper()
        else:
            print(f"Error: Parámetro desconocido '{args[i]}'.")
            sys.exit(1)
        i += 1

    if modo is None:
        print("Error: Debes indicar -c (cifrar) o -d (descifrar).")
        sys.exit(1)
    if texto is None:
        print("Error: Falta el texto a procesar.")
        sys.exit(1)
    if clave is None:
        print("Error: Falta la clave (-k).")
        sys.exit(1)

    return modo, texto, clave


if __name__ == "__main__":
    args = sys.argv[1:]

    if not args:
        print(__doc__)
        sys.exit(0)

    modo, texto, clave = parsear_argumentos(args)

    try:
        validar_texto(texto, "mensaje")
        validar_texto(clave, "clave")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    if modo == "cifrar":
        resultado = cifrar(texto, clave)
        mostrar_tabla(texto, clave, resultado, "cifrar")
    else:
        resultado = descifrar(texto, clave)
        mostrar_tabla(texto, clave, resultado, "descifrar")
