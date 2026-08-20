import pandas as pd

# ── Carga del fichero ──────────────────────────────────────────────────────────
df = pd.read_csv('house.csv')

print("=" * 55)
print("EJERCICIO 4 — Operaciones con fechas")
print("=" * 55)

# ── Convertir columna 'date' a tipo fecha ─────────────────────────────────────
print(f"\nTipo original de 'date': {df['date'].dtype}")
print(f"Muestra original:        {df['date'].head(3).tolist()}")

# El formato habitual en house.csv es '20141013T000000'
df['date'] = pd.to_datetime(df['date'], format='mixed', dayfirst=False)

print(f"\nTipo tras conversión:    {df['date'].dtype}")
print(f"Muestra convertida:      {df['date'].head(3).tolist()}")

# ── Extraer año, mes y día en nuevas columnas ────────────────────────────────
df['year']  = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day']   = df['date'].dt.day

print("\n── Columnas year / month / day (primeras 8 filas) ──")
print(df[['date', 'year', 'month', 'day']].head(8).to_string(index=True))

# ── Precio medio por mes ──────────────────────────────────────────────────────
precio_por_mes = (df.groupby('month')['price']
                    .mean()
                    .round(2)
                    .reset_index()
                    .rename(columns={'month': 'Mes', 'price': 'Precio medio (€)'}))

meses_nombre = {1:'Enero',2:'Febrero',3:'Marzo',4:'Abril',5:'Mayo',6:'Junio',
                7:'Julio',8:'Agosto',9:'Septiembre',10:'Octubre',11:'Noviembre',12:'Diciembre'}
precio_por_mes['Mes'] = precio_por_mes['Mes'].map(meses_nombre)

print("\n── Precio medio por mes ──")
print(precio_por_mes.to_string(index=False))

# ── Nueva columna date2 = date + 20 días ─────────────────────────────────────
df['date2'] = df['date'] + pd.Timedelta(days=20)

print("\n── Columna 'date2' (date + 20 días) — primeras 8 filas ──")
print(df[['date', 'date2']].head(8).to_string(index=True))
