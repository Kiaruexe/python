import pandas as pd

# ── Carga del fichero ──────────────────────────────────────────────────────────
df = pd.read_csv('house.csv')

print("=" * 55)
print("EJERCICIO 1 — Análisis básico de house.csv")
print("=" * 55)
print(f"\nForma del DataFrame: {df.shape}")
print(f"Columnas: {list(df.columns)}\n")

# ── ¿Hay alguna casa con 8 habitaciones? ──────────────────────────────────────
casas_8 = df[df['bedrooms'] == 8]
print("── ¿Hay casas con 8 habitaciones? ──")
if casas_8.empty:
    print("  No hay ninguna casa con 8 habitaciones.\n")
else:
    print(f"  Sí, hay {len(casas_8)} casa(s) con 8 habitaciones.")
    print(casas_8[['price', 'bedrooms', 'bathrooms', 'sqft_living']].to_string(index=True))
    print()

# ── Número mínimo y máximo de habitaciones ────────────────────────────────────
min_hab = df['bedrooms'].min()
max_hab = df['bedrooms'].max()
print("── Mínimo y máximo de habitaciones ──")
print(f"  Mínimo: {min_hab} habitaciones")
print(f"  Máximo: {max_hab} habitaciones\n")

# ── Nueva columna: precio por planta ──────────────────────────────────────────
# 'floors' indica el número de plantas evitamos división por cero
df['price_per_floor'] = df.apply(
    lambda row: round(row['price'] / row['floors'], 2) if row['floors'] > 0 else None,
    axis=1
)

print("── Nueva columna 'price_per_floor' (precio / plantas) ──")
print(df[['price', 'floors', 'price_per_floor']].head(10).to_string(index=True))
print(f"\n  Media precio por planta: {df['price_per_floor'].mean():,.2f} €")
