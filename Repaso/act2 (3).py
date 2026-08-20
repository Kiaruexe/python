import pandas as pd

# ── Carga del fichero ──────────────────────────────────────────────────────────
df = pd.read_csv('house.csv')

print("=" * 55)
print("EJERCICIO 2 — Selección e indexación")
print("=" * 55)

# ── Precio de la casa en la fila 256 ──────────────────────────────────────────
precio_256 = df.iloc[256]['price']
print(f"\n── Precio de la casa en la fila 256 ──")
print(f"  Precio: {precio_256:,.2f} €")

# ── Número de habitaciones de las filas 215 a 222 ────────────────────────────
print(f"\n── Habitaciones en las filas 215–222 ──")
print(df.iloc[215:223][['bedrooms']].to_string(index=True))

# ── Selección aleatoria del 15% del DF ───────────────────────────────────────
df_15 = df.sample(frac=0.15, random_state=42)
print(f"\n── Muestra aleatoria del 15% ──")
print(f"  Registros totales: {len(df)}")
print(f"  Registros en el 15%: {len(df_15)}")
print(df_15[['price', 'bedrooms', 'bathrooms', 'sqft_living']].head(8).to_string(index=True))

# ── Filtro: 3 o 4 habitaciones y precio < 300 000 € ──────────────────────────
print(f"\n── Del 15%: 3–4 habitaciones y precio < 300 000 € ──")

# Solución a
filtro_a = df_15[(df_15['bedrooms'].isin([3, 4])) & (df_15['price'] < 300_000)]
print(f"\n  Solución a  →  {len(filtro_a)} registro(s):")
print(filtro_a[['price', 'bedrooms', 'bathrooms', 'sqft_living']].to_string(index=True))

# Solución alternativa (misma lógica, sintaxis diferente)
mask_hab   = (df_15['bedrooms'] == 3) | (df_15['bedrooms'] == 4)
mask_precio = df_15['price'] < 300_000
filtro_alt = df_15[mask_hab & mask_precio]
print(f"\n  Solución alternativa  →  {len(filtro_alt)} registro(s):")
print(filtro_alt[['price', 'bedrooms', 'bathrooms', 'sqft_living']].to_string(index=True))
