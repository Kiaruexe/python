# =============================================================
# Ejercicio 5 — Dataset de Aeropuertos (OpenFlights)
# https://github.com/jpatokal/openflights/raw/master/data/airports-extended.dat
# =============================================================


# ============================================================
# 1. Carga del dataset como dataframe
# ============================================================

import pandas as pd

url = "https://github.com/jpatokal/openflights/raw/master/data/airports-extended.dat"

# El fichero no tiene cabecera, por eso definimos los nombres manualmente
columnas = ["AirportID", "Name", "City", "Country", "IATA", "ICAO",
            "Latitude", "Longitude", "Altitude", "Timezone", "DST", "Tz", "Type", "Source"]

df_aeropuertos = pd.read_csv(url, header=None, names=columnas)
print(f"Dataset cargado: {df_aeropuertos.shape[0]} filas, {df_aeropuertos.shape[1]} columnas")

# ============================================================
# 2. Primeras 10 filas del dataframe
# ============================================================

df_aeropuertos.head(10)

# ============================================================
# 3. Resumen estadístico inicial
# ============================================================

# include='all' muestra estadísticas de columnas numéricas y de texto
df_aeropuertos.describe(include="all")

# ============================================================
# 4. Eliminar columnas no necesarias
# ============================================================

# Primero hacemos una copia para no modificar el dataframe original
df_aeropuertos = df_aeropuertos.copy()

# Eliminamos las columnas que no vamos a emplear
columnas_a_eliminar = ["AirportID", "Latitude", "Longitude", "Altitude"]
df_aeropuertos.drop(columns=columnas_a_eliminar, inplace=True)

print(f"Columnas actuales ({len(df_aeropuertos.columns)}): {list(df_aeropuertos.columns)}")

# ============================================================
# 5. Nuevo resumen estadístico tras eliminar columnas
# ============================================================

df_aeropuertos.describe(include="all")

# ¿Cómo han cambiado los datos?
# - Antes teníamos 14 columnas (4 numéricas: AirportID, Latitude, Longitude, Altitude);
#   ahora tenemos 10 columnas.
# - El resumen ya no muestra mean/std/min/max de latitud, longitud, altitud ni ID numérico.
# - Quedan principalmente variables nominales/categóricas y Timezone (numérico).
# - La columna 'count' puede haber cambiado si esas columnas tenían nulos.

# ============================================================
# 6. Revisar el valor \N en la columna Tz con value_counts
# ============================================================

# Si no usamos na_values al cargar, el valor \N aparece como cadena de texto literal
# Revisamos la proporción de valores en la columna Tz
print("=== value_counts columna Tz (top 20) ===")
print(df_aeropuertos["Tz"].value_counts(dropna=False).head(20))

# Cuántos registros tienen exactamente el valor '\N' (cadena)
valor_raro = df_aeropuertos["Tz"].value_counts(dropna=False)
if "\\N" in valor_raro.index:
    print(f"\nRegistros con valor literal '\\N': {valor_raro['\\N']}")
    print(f"Proporción: {valor_raro['\\N'] / len(df_aeropuertos) * 100:.2f}%")

# ============================================================
# 7. Recargar el dataset interpretando correctamente los valores nulos
# ============================================================

# Recargamos pasando na_values='\\N' para que ese valor se interprete como NaN real
df_aeropuertos = pd.read_csv(
    url,
    header=None,
    names=columnas,
    na_values="\\N"   # '\N' en el CSV se convierte en NaN
)

# Volvemos a eliminar las columnas no necesarias
df_aeropuertos.drop(columns=["AirportID", "Latitude", "Longitude", "Altitude"], inplace=True)

# Verificamos que ahora los nulos son NaN reales
print("Nulos (NaN) por columna tras la recarga:")
print(df_aeropuertos.isnull().sum())

# ============================================================
# 8. Función para revisar value_counts de cada columna
# ============================================================

def value_counts_todas(df, columnas=None, top_n=10):
    """
    Muestra los value_counts de cada columna del dataframe.

    Parámetros
    ----------
    df      : DataFrame de pandas
    columnas: lista de columnas a revisar (por defecto todas)
    top_n   : número de valores más frecuentes a mostrar por columna
    """
    if columnas is None:
        columnas = df.columns

    for col in columnas:
        print(f"\n{'='*55}")
        print(f"  Columna: {col}  |  Nulos: {df[col].isna().sum()}  |  Únicos: {df[col].nunique()}")
        print(f"{'='*55}")
        print(df[col].value_counts(dropna=False).head(top_n))


# Llamamos a la función con todas las columnas del dataframe
value_counts_todas(df_aeropuertos)

# ============================================================
# 9. Función para sobreescribir valores nulos con un valor dado
# ============================================================

def rellenar_nulos(df, columnas, valor):
    """
    Sobreescribe los valores nulos (NaN) de las columnas indicadas con el valor dado.

    Parámetros
    ----------
    df      : DataFrame de pandas
    columnas: str o lista de str con los nombres de columna
    valor   : valor con el que reemplazar los NaN
    """
    if isinstance(columnas, str):
        columnas = [columnas]

    for col in columnas:
        nulos_antes = df[col].isna().sum()
        df[col].fillna(valor, inplace=True)
        print(f"Columna '{col}': {nulos_antes} nulos → reemplazados por '{valor}'")

    return df


# Sobreescribimos los nulos de IATA e ICAO por 'DESCONOCIDO'
df_aeropuertos = rellenar_nulos(df_aeropuertos, ["IATA", "ICAO"], "DESCONOCIDO")

# Verificamos
print(f"\nNulos restantes en IATA: {df_aeropuertos['IATA'].isna().sum()}")
print(f"Nulos restantes en ICAO: {df_aeropuertos['ICAO'].isna().sum()}")

# ============================================================
# 10. Función para cambiar el tipo de datos de una columna
# ============================================================

def cambiar_tipo(df, columnas, nuevo_tipo):
    """
    Cambia el tipo de datos de las columnas indicadas.

    Parámetros
    ----------
    df         : DataFrame de pandas
    columnas   : str o lista de str con los nombres de columna
    nuevo_tipo : tipo destino, p.ej. 'category', 'int', 'float', 'str'
    """
    if isinstance(columnas, str):
        columnas = [columnas]

    for col in columnas:
        tipo_antes = df[col].dtype
        df[col] = df[col].astype(nuevo_tipo)
        print(f"Columna '{col}': {tipo_antes} → {df[col].dtype}")

    return df


# Convertimos DST y Tz a tipo categórico
df_aeropuertos = cambiar_tipo(df_aeropuertos, ["DST", "Tz"], "category")

# Verificamos
print("\nTipos de columnas DST y Tz:")
print(df_aeropuertos[["DST", "Tz"]].dtypes)

# ============================================================
# 11. Función para resumen estadístico de variables categóricas
# ============================================================

def resumen_categoricas(df):
    """
    Muestra un resumen estadístico de todas las columnas categóricas del dataframe.
    Incluye columnas de tipo 'category' y 'object'.
    """
    cols_cat = df.select_dtypes(include=["category", "object"]).columns

    if len(cols_cat) == 0:
        print("No hay columnas categóricas en el dataframe.")
        return

    print(f"Variables categóricas encontradas ({len(cols_cat)}): {list(cols_cat)}\n")
    return df[cols_cat].describe()


resumen_categoricas(df_aeropuertos)

# ============================================================
# 12. Función para agrupar y contar por cualquier campo
# ============================================================

def agrupar_conteo(df, columna):
    """
    Agrupa el dataframe por la columna indicada y muestra el conteo de registros.

    Parámetros
    ----------
    df      : DataFrame de pandas
    columna : nombre de la columna por la que agrupar
    """
    conteo = df.groupby(columna, observed=True).size().reset_index(name="conteo")
    conteo = conteo.sort_values("conteo", ascending=False).reset_index(drop=True)
    print(f"Agrupación por '{columna}':")
    print(conteo.to_string(index=False))
    return conteo


# Agrupamos por tipo de aeropuerto
agrupar_conteo(df_aeropuertos, "Type")

# ============================================================
# 13. Ciudades cuyo tipo de aeropuerto es 'port'
# ============================================================

ciudades_port = df_aeropuertos[df_aeropuertos["Type"] == "port"]["City"]
print(f"Ciudades con tipo 'port' ({len(ciudades_port)} registros):")
print(ciudades_port.values)

# ============================================================
# 14. Aeropuertos cuyo país es Spain
# ============================================================

espana = df_aeropuertos[
    df_aeropuertos["Country"] == "Spain"
][["Name", "Country", "City", "Type"]]

print(f"Total de registros en Spain: {len(espana)}")
espana

# ============================================================
# 15. Aeropuertos de Madrid y Barcelona
# ============================================================

madrid_bcn = df_aeropuertos[
    df_aeropuertos["City"].isin(["Madrid", "Barcelona"])
][["Country", "Name", "City", "Type"]]

print(f"Registros encontrados: {len(madrid_bcn)}")
print(madrid_bcn.to_string())

print("\n¿Todos los registros son de España?")
todos_espana = (madrid_bcn["Country"] == "Spain").all()
if todos_espana:
    print("→ Sí, todos los registros pertenecen a Spain.")
else:
    otros = madrid_bcn[madrid_bcn["Country"] != "Spain"]
    print(f"→ No. Hay {len(otros)} registros de otros países:")
    print(otros)

# ============================================================
# 16. Guardar los resultados en CSV y Excel
# ============================================================

# Guardamos en CSV
madrid_bcn.to_csv("Madrid_Barcelona.csv", index=False)
print("Guardado: Madrid_Barcelona.csv")

# Guardamos en Excel
madrid_bcn.to_excel("Madrid_Barcelona.xlsx", index=False)
print("Guardado: Madrid_Barcelona.xlsx")