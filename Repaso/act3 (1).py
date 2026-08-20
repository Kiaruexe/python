import pandas as pd

# ── Carga del fichero ──────────────────────────────────────────────────────────
df = pd.read_csv('house.csv')

print("=" * 55)
print("EJERCICIO 3 — Índice múltiple (MultiIndex)")
print("=" * 55)

# ── Definición de columnas por grupo ─────────────────────────────────────────
cols_localizacion   = ['street', 'city', 'statezip', 'country']
cols_caracteristicas = [c for c in df.columns if c not in cols_localizacion]

print(f"\nColumnas de localización:    {cols_localizacion}")
print(f"Columnas de características: {cols_caracteristicas}")

# ── Creación del MultiIndex con pd.MultiIndex.from_arrays ─────────────────────
# Construimos un MultiIndex de columnas agrupando cada columna bajo su categoría
tuples = ([(  'localizacion', col) for col in sorted(cols_localizacion)]
        + [('caracteristicas', col) for col in sorted(cols_caracteristicas)])

multi_index = pd.MultiIndex.from_tuples(tuples)

# Reordenamos las columnas del DF según los tuples y asignamos el MultiIndex
cols_ordenadas = [t[1] for t in tuples]
df_multi = df[cols_ordenadas].copy()
df_multi.columns = multi_index

print("\n── Vista general del MultiIndex ──")
print(df_multi.head(5).to_string())

# ── DF solo con columnas de localización ──────────────────────────────────────
df_loc = df_multi['localizacion']

print(f"\n── DF con solo columnas de 'localizacion' ({df_loc.shape}) ──")
print(df_loc.head(10).to_string(index=True))

print(f"\nTipo del índice de columnas: {type(df_multi.columns)}")
print(f"Niveles: {df_multi.columns.names}")
