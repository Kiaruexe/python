import numpy as np

# Creación del array 2D 5x5 con 25 números aleatorios entre los 100 primeros
arr = np.random.choice(range(1, 101), size=25, replace=True).reshape(5, 5)

# 1) Pintar la matriz resultante
print("1) Matriz original (5x5):")
print(arr)

# 2) Valores múltiplos de 5
mult5 = arr[arr % 5 == 0]
print("\n2) Múltiplos de 5:")
print(mult5)

# 3) Valores pares o impares menores de 10
#    (pares O impares = todos) -> equivale a todos los menores de 10
men10 = arr[arr < 10]
print("\n3) Pares o impares menores de 10 (todos los <10):")
print(men10)

# 4) Múltiplos de 3, impares y mayores de 20
mult3_imp_may20 = arr[(arr % 3 == 0) & (arr % 2 != 0) & (arr > 20)]
print("\n4) Múltiplos de 3, impares y >20:")
print(mult3_imp_may20)

# 5) Unión de los tres resultados — valores únicos en array 1D
union = np.unique(np.concatenate([mult5, men10, mult3_imp_may20]))
print("\n5) Unión única (array 1D):")
print(union)

# 6) Reestructurar a 2D con tantas filas como elementos (Nx1)
arr2d = union.reshape(-1, 1)
print("\n6) Array 2D restructurado ({} filas x 1 columna):".format(arr2d.shape[0]))
print(arr2d)

# 7) Estructura, dimensiones y número de elementos
print("\n7) Información del nuevo array 2D:")
print("   ndim  :", arr2d.ndim)
print("   shape :", arr2d.shape)
print("   size  :", arr2d.size)
print("   dtype :", arr2d.dtype)
