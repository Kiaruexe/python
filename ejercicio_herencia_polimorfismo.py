# ── Clase base 1: Mamifero ─────────────────────────────────────────────────────
class Mamifero:
    def __init__(self, patas: int, pelaje: str):
        self.patas  = patas
        self.pelaje = pelaje

    def amamantar(self):
        print("El mamífero está amamantando a sus crías.")

    def dormir(self):
        print("El mamífero está durmiendo.")


# ── Clase base 2: AnimalDomestico ─────────────────────────────────────────────
class AnimalDomestico:
    def __init__(self, dueno: str, nombre: str):
        self.dueno  = dueno
        self.nombre = nombre

    def entrenar(self):
        print(f"El animal {self.nombre} está siendo entrenado por {self.dueno}.")

    def poner_vacunas(self):
        print(f"Poniendo vacunas a {self.nombre}.")

    def comer(self, alimento: str):
        print(f"El animal {self.nombre} está comiendo {alimento}.")


# ── Clase Perro: hereda de Mamifero y AnimalDomestico ─────────────────────────
class Perro(Mamifero, AnimalDomestico):
    def __init__(self, nombre: str, dueno: str, pelaje: str):
        Mamifero.__init__(self, patas=4, pelaje=pelaje)
        AnimalDomestico.__init__(self, dueno=dueno, nombre=nombre)

    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau Guau Guau!")

    def jugar(self):
        print(f"El perro {self.nombre} está jugando.")


# ── Clase Gato: hereda de Mamifero y AnimalDomestico ──────────────────────────
class Gato(Mamifero, AnimalDomestico):
    def __init__(self, nombre: str, dueno: str, pelaje: str):
        Mamifero.__init__(self, patas=4, pelaje=pelaje)
        AnimalDomestico.__init__(self, dueno=dueno, nombre=nombre)

    def maullar(self):
        print(f"{self.nombre} dice: ¡Miau Miau Miau!")

    def cazar(self):
        print(f"El gato {self.nombre} está cazando.")


# ── Prueba ─────────────────────────────────────────────────────────────────────
bobi  = Perro(nombre="Bobi",  dueno="Carlos", pelaje="Negro")
luna  = Perro(nombre="Luna",  dueno="Marta",  pelaje="Marrón")
misi  = Gato(nombre="Misi",  dueno="Laura",  pelaje="Gris")
felix = Gato(nombre="Félix", dueno="Javier", pelaje="Naranja")

animales = [bobi, luna, misi, felix]

print("=" * 50)
for animal in animales:
    print(f"\n>>> {animal.nombre} ({animal.__class__.__name__})")
    animal.amamantar()
    animal.dormir()
    animal.entrenar()
    animal.poner_vacunas()
    animal.comer("pienso")

    if isinstance(animal, Perro):
        animal.ladrar()
        animal.jugar()
    elif isinstance(animal, Gato):
        animal.maullar()
        animal.cazar()
