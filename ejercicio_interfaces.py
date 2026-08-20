from abc import ABC, abstractmethod


# ── Interfaz: AdaptadorBaseDatos ───────────────────────────────────────────────
class AdaptadorBaseDatos(ABC):

    @abstractmethod
    def conectar(self):
        """Establece la conexión con la base de datos."""
        pass

    @abstractmethod
    def ejecutar_consulta(self, consulta: str):
        """Ejecuta una consulta sobre la base de datos."""
        pass

    @abstractmethod
    def cerrar_conexion(self):
        """Cierra la conexión con la base de datos."""
        pass


# ── Implementación 1: MySQL ────────────────────────────────────────────────────
class AdaptadorMySQL(AdaptadorBaseDatos):

    def __init__(self, host: str, usuario: str, contrasena: str, base_datos: str):
        self.host        = host
        self.usuario     = usuario
        self.contrasena  = contrasena
        self.base_datos  = base_datos
        self.conectado   = False

    def conectar(self):
        self.conectado = True
        print(f"[MySQL] Conectado a '{self.base_datos}' en {self.host} "
              f"como usuario '{self.usuario}'.")

    def ejecutar_consulta(self, consulta: str):
        if not self.conectado:
            print("[MySQL] Error: no hay conexión activa.")
            return
        print(f"[MySQL] Ejecutando consulta: {consulta}")

    def cerrar_conexion(self):
        self.conectado = False
        print(f"[MySQL] Conexión con '{self.base_datos}' cerrada.")


# ── Implementación 2: PostgreSQL ───────────────────────────────────────────────
class AdaptadorPostgreSQL(AdaptadorBaseDatos):

    def __init__(self, host: str, puerto: int, usuario: str, contrasena: str, base_datos: str):
        self.host        = host
        self.puerto      = puerto
        self.usuario     = usuario
        self.contrasena  = contrasena
        self.base_datos  = base_datos
        self.conectado   = False

    def conectar(self):
        self.conectado = True
        print(f"[PostgreSQL] Conectado a '{self.base_datos}' en {self.host}:{self.puerto} "
              f"como usuario '{self.usuario}'.")

    def ejecutar_consulta(self, consulta: str):
        if not self.conectado:
            print("[PostgreSQL] Error: no hay conexión activa.")
            return
        print(f"[PostgreSQL] Ejecutando consulta: {consulta}")

    def cerrar_conexion(self):
        self.conectado = False
        print(f"[PostgreSQL] Conexión con '{self.base_datos}' cerrada.")


# ── Implementación 3: SQLite ───────────────────────────────────────────────────
class AdaptadorSQLite(AdaptadorBaseDatos):

    def __init__(self, ruta_archivo: str):
        self.ruta_archivo = ruta_archivo
        self.conectado    = False

    def conectar(self):
        self.conectado = True
        print(f"[SQLite] Conectado al archivo de base de datos: '{self.ruta_archivo}'.")

    def ejecutar_consulta(self, consulta: str):
        if not self.conectado:
            print("[SQLite] Error: no hay conexión activa.")
            return
        print(f"[SQLite] Ejecutando consulta: {consulta}")

    def cerrar_conexion(self):
        self.conectado = False
        print(f"[SQLite] Conexión con '{self.ruta_archivo}' cerrada.")


# ── Prueba ─────────────────────────────────────────────────────────────────────
adaptadores = [
    AdaptadorMySQL(
        host="localhost", usuario="root",
        contrasena="1234", base_datos="tienda"
    ),
    AdaptadorPostgreSQL(
        host="192.168.1.10", puerto=5432, usuario="admin",
        contrasena="abcd", base_datos="inventario"
    ),
    AdaptadorSQLite(ruta_archivo="datos_locales.db"),
]

consulta_prueba = "SELECT * FROM productos"

print("=" * 55)
for adaptador in adaptadores:
    print()
    adaptador.conectar()
    adaptador.ejecutar_consulta(consulta_prueba)
    adaptador.cerrar_conexion()
print("=" * 55)
