import numpy as np

# 1) Crear arrays a y b
a = np.random.randn(3, 3)           # 2D normal, estructura 3x3
b = np.random.uniform(3, 6, size=3) # 1D con 3 elementos entre 3-6

print("1) Array a (3x3, valores normales):")
print(np.round(a, 4))
print("\n1) Array b (1D, 3 elementos entre 3-6):")
print(np.round(b, 4))

# 2) Suma de a+b y aplicar raíz cuadrada
#    np.abs para evitar NaN cuando la suma produce valores negativos
suma = a + b                        # broadcasting: b se suma a cada fila de a
result = np.sqrt(np.abs(suma))

# 3) Redondear a dos decimales
result = np.round(result, 2)
print("\n2-3) sqrt(a + b) redondeado a 2 decimales:")
print(result)

# 4) Array c — 2D 5x5 con números aleatorios entre 0-60
c = np.random.randint(0, 61, size=(5, 5))
print("\n4) Array c (5x5, entre 0-60):")
print(c)

# 5) Ordenar cada fila
c_sorted = np.sort(c, axis=1)
print("\n5) c con filas ordenadas:")
print(c_sorted)

# 6) Inversas del array resultante del apartado 5
# 6a) Inversa de cada fila (invertir elementos dentro de cada fila)
inv_filas = c_sorted[:, ::-1]
print("\n6a) Inversa de cada fila:")
print(inv_filas)

# 6b) Inversa de cada columna (invertir el orden de las filas)
inv_cols = c_sorted[::-1, :]
print("\n6b) Inversa de cada columna:")
print(inv_cols)

# 6c) Inversa de toda la matriz (invertir filas y columnas a la vez)
inv_todo = c_sorted[::-1, ::-1]
print("\n6c) Inversa de toda la matriz:")
print(inv_todo)

# 7) Traspuesta de c
c_T = c.T
print("\n7) Traspuesta de c:")
print(c_T)
print("   Shape original :", c.shape)
print("   Shape traspuesta:", c_T.shape)
