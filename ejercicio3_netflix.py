"""
Ejercicio 3 - Netflix
Simulación de altas/bajas de socios y películas en una plataforma tipo Netflix.
"""


# =============================================================
# CLASE: Pelicula
# =============================================================

class Pelicula:
    """Representa una película disponible en la plataforma."""

    def __init__(self, titulo, genero, anio, duracion_min, director):
        self.titulo = titulo
        self.genero = genero
        self.anio = anio
        self.duracion_min = duracion_min
        self.director = director

    def __str__(self):
        return (
            f"🎬 {self.titulo} ({self.anio})\n"
            f"   Género   : {self.genero}\n"
            f"   Director : {self.director}\n"
            f"   Duración : {self.duracion_min} min"
        )

    def __eq__(self, other):
        """Dos películas son iguales si tienen el mismo título y año."""
        if isinstance(other, Pelicula):
            return self.titulo.lower() == other.titulo.lower() and self.anio == other.anio
        return False


# =============================================================
# CLASE: Socio
# =============================================================

class Socio:
    """Representa un socio de la plataforma Netflix."""

    PLANES = {"basico", "estandar", "premium"}

    def __init__(self, nombre, email, plan="basico"):
        self.nombre = nombre
        self.email = email
        self.plan = plan if plan in self.PLANES else "basico"
        self.peliculas_vistas = []

    def ver_pelicula(self, pelicula):
        """Registra una película como vista por el socio."""
        if isinstance(pelicula, Pelicula):
            self.peliculas_vistas.append(pelicula)
            print(f"✅ {self.nombre} ha visto '{pelicula.titulo}'.")
        else:
            print("❌ El objeto proporcionado no es una película válida.")

    def historial(self):
        """Muestra el historial de películas vistas."""
        if not self.peliculas_vistas:
            print(f"📋 {self.nombre} aún no ha visto ninguna película.")
        else:
            print(f"📋 Historial de {self.nombre}:")
            for i, p in enumerate(self.peliculas_vistas, 1):
                print(f"  {i}. {p.titulo} ({p.anio})")

    def cambiar_plan(self, nuevo_plan):
        """Cambia el plan de suscripción del socio."""
        if nuevo_plan in self.PLANES:
            antiguo = self.plan
            self.plan = nuevo_plan
            print(f"🔄 {self.nombre}: plan cambiado de '{antiguo}' a '{nuevo_plan}'.")
        else:
            print(f"❌ Plan '{nuevo_plan}' no válido. Opciones: {', '.join(self.PLANES)}")

    def __str__(self):
        return (
            f"👤 {self.nombre}\n"
            f"   Email    : {self.email}\n"
            f"   Plan     : {self.plan}\n"
            f"   Vistas   : {len(self.peliculas_vistas)} película(s)"
        )

    def __eq__(self, other):
        """Dos socios son iguales si tienen el mismo email."""
        if isinstance(other, Socio):
            return self.email.lower() == other.email.lower()
        return False

    def __lt__(self, other):
        """Permite ordenar socios por nombre."""
        if isinstance(other, Socio):
            return self.nombre.lower() < other.nombre.lower()
        return NotImplemented


# =============================================================
# CLASE: Netflix
# =============================================================

class Netflix:
    """
    Simula la plataforma Netflix con gestión de socios y películas.

    Atributos:
    -----------
    socios    : lista de objetos Socio
    peliculas : lista de objetos Pelicula
    """

    def __init__(self, nombre_plataforma="Netflix"):
        self.nombre_plataforma = nombre_plataforma
        self.socios = []
        self.peliculas = []

    # ----------------------------------------------------------
    # GESTIÓN DE SOCIOS
    # ----------------------------------------------------------

    def alta_socio(self, socio):
        """Registra un nuevo socio en la plataforma."""
        if not isinstance(socio, Socio):
            print("❌ El objeto proporcionado no es un socio válido.")
            return
        if socio in self.socios:
            print(f"⚠️  El socio '{socio.nombre}' (email: {socio.email}) ya está registrado.")
        else:
            self.socios.append(socio)
            print(f"✅ Socio '{socio.nombre}' registrado correctamente.")

    def baja_socio(self, email):
        """Elimina un socio de la plataforma por su email."""
        for socio in self.socios:
            if socio.email.lower() == email.lower():
                self.socios.remove(socio)
                print(f"✅ Socio '{socio.nombre}' dado de baja correctamente.")
                return
        print(f"⚠️  No se encontró ningún socio con el email '{email}'.")

    def buscar_socio(self, email):
        """Devuelve el socio con ese email o None si no existe."""
        for socio in self.socios:
            if socio.email.lower() == email.lower():
                return socio
        return None

    def listar_socios(self):
        """Muestra todos los socios registrados."""
        print(f"\n{'='*50}")
        print(f"  👥 SOCIOS DE {self.nombre_plataforma.upper()}")
        print(f"{'='*50}")
        if not self.socios:
            print("  No hay socios registrados.")
        else:
            for socio in sorted(self.socios):
                print(socio)
                print()
        print("=" * 50)

    # ----------------------------------------------------------
    # GESTIÓN DE PELÍCULAS
    # ----------------------------------------------------------

    def alta_pelicula(self, pelicula):
        """Añade una nueva película al catálogo."""
        if not isinstance(pelicula, Pelicula):
            print("❌ El objeto proporcionado no es una película válida.")
            return
        if pelicula in self.peliculas:
            print(f"⚠️  La película '{pelicula.titulo}' ({pelicula.anio}) ya está en el catálogo.")
        else:
            self.peliculas.append(pelicula)
            print(f"✅ Película '{pelicula.titulo}' añadida al catálogo.")

    def baja_pelicula(self, titulo, anio):
        """Elimina una película del catálogo por título y año."""
        for pelicula in self.peliculas:
            if pelicula.titulo.lower() == titulo.lower() and pelicula.anio == anio:
                self.peliculas.remove(pelicula)
                print(f"✅ Película '{pelicula.titulo}' ({anio}) eliminada del catálogo.")
                return
        print(f"⚠️  No se encontró la película '{titulo}' ({anio}) en el catálogo.")

    def buscar_pelicula(self, titulo):
        """Busca películas por título (búsqueda parcial, insensible a mayúsculas)."""
        resultados = [p for p in self.peliculas if titulo.lower() in p.titulo.lower()]
        return resultados

    def listar_peliculas(self):
        """Muestra todas las películas del catálogo."""
        print(f"\n{'='*50}")
        print(f"  🎬 CATÁLOGO DE {self.nombre_plataforma.upper()}")
        print(f"{'='*50}")
        if not self.peliculas:
            print("  No hay películas en el catálogo.")
        else:
            for pelicula in sorted(self.peliculas, key=lambda p: p.titulo.lower()):
                print(pelicula)
                print()
        print("=" * 50)

    def peliculas_por_genero(self, genero):
        """Devuelve y muestra las películas de un género concreto."""
        resultados = [p for p in self.peliculas if p.genero.lower() == genero.lower()]
        print(f"\n🎭 Películas del género '{genero}':")
        if resultados:
            for p in resultados:
                print(f"  - {p.titulo} ({p.anio})")
        else:
            print("  No se encontraron películas de ese género.")
        return resultados

    def __str__(self):
        return (
            f"🌐 Plataforma : {self.nombre_plataforma}\n"
            f"   Socios     : {len(self.socios)}\n"
            f"   Películas  : {len(self.peliculas)}"
        )


# =============================================================
# PROGRAMA PRINCIPAL (demostración)
# =============================================================

if __name__ == "__main__":

    print("\n" + "=" * 60)
    print("  DEMO: SIMULACIÓN NETFLIX")
    print("=" * 60)

    # --- Crear la plataforma ---
    netflix = Netflix("MyFlix")

    # --- Crear películas ---
    p1 = Pelicula("El Padrino", "Drama", 1972, 175, "Francis Ford Coppola")
    p2 = Pelicula("Inception", "Ciencia Ficcion", 2010, 148, "Christopher Nolan")
    p3 = Pelicula("Pulp Fiction", "Thriller", 1994, 154, "Quentin Tarantino")
    p4 = Pelicula("Interstellar", "Ciencia Ficcion", 2014, 169, "Christopher Nolan")
    p5 = Pelicula("La La Land", "Musical", 2016, 128, "Damien Chazelle")

    # --- Dar de alta películas ---
    print("\n--- Alta de peliculas ---\n")
    for pelicula in [p1, p2, p3, p4, p5]:
        netflix.alta_pelicula(pelicula)

    # Intentar añadir una película duplicada
    netflix.alta_pelicula(Pelicula("Inception", "Ciencia Ficcion", 2010, 148, "Christopher Nolan"))

    # --- Listar películas ---
    netflix.listar_peliculas()

    # --- Crear socios ---
    s1 = Socio("Ana Garcia", "ana@email.com", "premium")
    s2 = Socio("Carlos Lopez", "carlos@email.com", "estandar")
    s3 = Socio("Beatriz Ruiz", "beatriz@email.com", "basico")

    # --- Dar de alta socios ---
    print("\n--- Alta de socios ---\n")
    for socio in [s1, s2, s3]:
        netflix.alta_socio(socio)

    # Intentar añadir un socio duplicado
    netflix.alta_socio(Socio("Ana Garcia Duplicada", "ana@email.com", "basico"))

    # --- Listar socios ---
    netflix.listar_socios()

    # --- Ver películas (registrar historial) ---
    print("\n--- Registro de visualizaciones ---\n")
    s1.ver_pelicula(p1)
    s1.ver_pelicula(p2)
    s2.ver_pelicula(p3)
    s3.ver_pelicula(p4)
    s3.ver_pelicula(p5)
    s3.ver_pelicula(p1)

    # --- Mostrar historial ---
    print()
    s1.historial()
    s2.historial()
    s3.historial()

    # --- Cambiar plan de suscripción ---
    print()
    s3.cambiar_plan("premium")
    s2.cambiar_plan("ultra")  # Plan inválido

    # --- Buscar películas por género ---
    netflix.peliculas_por_genero("Ciencia Ficcion")

    # --- Baja de película ---
    print("\n--- Baja de pelicula ---\n")
    netflix.baja_pelicula("Pulp Fiction", 1994)
    netflix.baja_pelicula("Matrix", 1999)  # No existe

    # --- Baja de socio ---
    print("\n--- Baja de socio ---\n")
    netflix.baja_socio("carlos@email.com")
    netflix.baja_socio("pepe@email.com")  # No existe

    # --- Estado final de la plataforma ---
    print(f"\n--- Estado final ---\n")
    print(netflix)
    netflix.listar_socios()
    netflix.listar_peliculas()
