from abc import ABC, abstractmethod


# ─────────────────────────────────────────────
# CLASE ABSTRACTA: Producto
# ─────────────────────────────────────────────

class Producto(ABC):
    """Clase abstracta base para todos los productos de la tienda."""

    def __init__(self, nombre, precio, descripcion, esta_oferta=False):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.esta_oferta = esta_oferta

    @abstractmethod
    def calcular_precio(self):
        """Calcula el precio final del producto."""
        pass

    @abstractmethod
    def mostrar_informacion(self):
        """Muestra por pantalla la información básica del producto."""
        pass


# ─────────────────────────────────────────────
# CLASES HIJAS
# ─────────────────────────────────────────────

class Libro(Producto):
    """Representa un libro vendido en la tienda."""

    DESCUENTO_OFERTA = 0.15  # 15% de descuento si está en oferta

    def __init__(self, nombre, precio, descripcion, autor, esta_oferta=False):
        super().__init__(nombre, precio, descripcion, esta_oferta)
        self.autor = autor

    def calcular_precio(self):
        if self.esta_oferta:
            return self.precio * (1 - self.DESCUENTO_OFERTA)
        return self.precio

    def mostrar_informacion(self):
        oferta_txt = "✅ En oferta" if self.esta_oferta else "❌ Sin oferta"
        print(f"📚 LIBRO: {self.nombre}")
        print(f"   Autor      : {self.autor}")
        print(f"   Descripción: {self.descripcion}")
        print(f"   Precio base: {self.precio:.2f} €")
        print(f"   Precio final: {self.calcular_precio():.2f} €  |  {oferta_txt}")
        print()


class Disco(Producto):
    """Representa un disco (álbum musical) vendido en la tienda."""

    DESCUENTO_OFERTA = 0.20  # 20% de descuento si está en oferta

    def __init__(self, nombre, precio, descripcion, artista, esta_oferta=False):
        super().__init__(nombre, precio, descripcion, esta_oferta)
        self.artista = artista

    def calcular_precio(self):
        if self.esta_oferta:
            return self.precio * (1 - self.DESCUENTO_OFERTA)
        return self.precio

    def mostrar_informacion(self):
        oferta_txt = "✅ En oferta" if self.esta_oferta else "❌ Sin oferta"
        print(f"🎵 DISCO: {self.nombre}")
        print(f"   Artista    : {self.artista}")
        print(f"   Descripción: {self.descripcion}")
        print(f"   Precio base: {self.precio:.2f} €")
        print(f"   Precio final: {self.calcular_precio():.2f} €  |  {oferta_txt}")
        print()


class Electronico(Producto):
    """Representa un producto electrónico vendido en la tienda."""

    DESCUENTO_OFERTA = 0.10  # 10% de descuento si está en oferta

    def __init__(self, nombre, precio, descripcion, marca, esta_oferta=False):
        super().__init__(nombre, precio, descripcion, esta_oferta)
        self.marca = marca

    def calcular_precio(self):
        if self.esta_oferta:
            return self.precio * (1 - self.DESCUENTO_OFERTA)
        return self.precio

    def mostrar_informacion(self):
        oferta_txt = "✅ En oferta" if self.esta_oferta else "❌ Sin oferta"
        print(f"💻 ELECTRÓNICO: {self.nombre}")
        print(f"   Marca      : {self.marca}")
        print(f"   Descripción: {self.descripcion}")
        print(f"   Precio base: {self.precio:.2f} €")
        print(f"   Precio final: {self.calcular_precio():.2f} €  |  {oferta_txt}")
        print()


# Clase hija adicional: Videojuego
class Videojuego(Producto):
    """Representa un videojuego vendido en la tienda."""

    DESCUENTO_OFERTA = 0.25  # 25% de descuento si está en oferta

    def __init__(self, nombre, precio, descripcion, plataforma, esta_oferta=False):
        super().__init__(nombre, precio, descripcion, esta_oferta)
        self.plataforma = plataforma

    def calcular_precio(self):
        if self.esta_oferta:
            return self.precio * (1 - self.DESCUENTO_OFERTA)
        return self.precio

    def mostrar_informacion(self):
        oferta_txt = "✅ En oferta" if self.esta_oferta else "❌ Sin oferta"
        print(f"🎮 VIDEOJUEGO: {self.nombre}")
        print(f"   Plataforma : {self.plataforma}")
        print(f"   Descripción: {self.descripcion}")
        print(f"   Precio base: {self.precio:.2f} €")
        print(f"   Precio final: {self.calcular_precio():.2f} €  |  {oferta_txt}")
        print()


# ─────────────────────────────────────────────
# CLASE: Tienda
# ─────────────────────────────────────────────

class Tienda:
    """Representa la tienda online con todos sus productos."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        """Agrega un producto a la tienda."""
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agregar instancias de Producto.")
        self.productos.append(producto)
        print(f"✔ Producto '{producto.nombre}' agregado correctamente.")

    def mostrar_productos(self):
        """Muestra por pantalla todos los productos de la tienda."""
        print("=" * 50)
        print(f"  🛒 PRODUCTOS EN {self.nombre.upper()}")
        print("=" * 50)
        if not self.productos:
            print("  La tienda no tiene productos aún.")
        else:
            for producto in self.productos:
                producto.mostrar_informacion()  # Polimorfismo
        print("=" * 50)

    def buscar_productos(self, termino):
        """Busca productos por nombre o descripción (insensible a mayúsculas)."""
        termino = termino.lower()
        resultados = [
            p for p in self.productos
            if termino in p.nombre.lower() or termino in p.descripcion.lower()
        ]
        print(f"\n🔍 Resultados para '{termino}':")
        if resultados:
            for p in resultados:
                p.mostrar_informacion()
        else:
            print("  No se encontraron productos.\n")
        return resultados

    def calcular_precio_total(self):
        """Calcula y muestra el precio total de todos los productos."""
        total = sum(p.calcular_precio() for p in self.productos)
        print(f"\n💰 Precio total de todos los productos: {total:.2f} €\n")
        return total


# ─────────────────────────────────────────────
# PROGRAMA PRINCIPAL (demostración)
# ─────────────────────────────────────────────

if __name__ == "__main__":

    # Crear la tienda
    tienda = Tienda("PyShop")

    # Crear productos
    libro1    = Libro("Cien años de soledad", 18.99, "Novela de Gabriel García Márquez", "Gabriel García Márquez", esta_oferta=True)
    libro2    = Libro("El Quijote", 12.50, "Clásico de la literatura española", "Miguel de Cervantes")
    disco1    = Disco("Thriller", 14.99, "Álbum icónico de pop/rock", "Michael Jackson", esta_oferta=True)
    disco2    = Disco("Back in Black", 11.99, "Álbum de hard rock", "AC/DC")
    electro1  = Electronico("iPhone 15", 999.00, "Smartphone de última generación", "Apple", esta_oferta=True)
    electro2  = Electronico("TV OLED 55\"", 1200.00, "Televisor OLED 4K 55 pulgadas", "LG")
    juego1    = Videojuego("The Legend of Zelda: TOTK", 59.99, "Aventura épica en mundo abierto", "Nintendo Switch", esta_oferta=True)

    # Agregar productos a la tienda
    print("\n--- Agregando productos ---\n")
    for producto in [libro1, libro2, disco1, disco2, electro1, electro2, juego1]:
        tienda.agregar_producto(producto)

    # Mostrar todos los productos
    print()
    tienda.mostrar_productos()

    # Buscar productos
    tienda.buscar_productos("rock")
    tienda.buscar_productos("Apple")

    # Calcular precio total
    tienda.calcular_precio_total()
