import random


class Objeto:
    def __init__(self, nombre_objeto, peso):
        self.nombre_objeto = nombre_objeto
        self.peso = peso

    def __str__(self):
        return f"{self.nombre_objeto} ({self.peso} kg)"


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        # Genera entre 1 y 5 objetos con peso aleatorio entre 1 y 10
        self.objetos = [
            Objeto(f"Objeto_{i+1}", random.randint(1, 10))
            for i in range(random.randint(1, 5))
        ]

    def peso_maximo_objeto(self):
        """Devuelve el peso del objeto más pesado que lleva esta persona."""
        return max(obj.peso for obj in self.objetos)

    def cantidad_objetos(self):
        """Devuelve el número de objetos que lleva esta persona."""
        return len(self.objetos)

    def __str__(self):
        objetos_str = ", ".join(str(obj) for obj in self.objetos)
        return (
            f"{self.nombre} (edad: {self.edad}) | "
            f"Objetos ({len(self.objetos)}): [{objetos_str}]"
        )


# --- Creación de personas ---
personas = [
    Persona("Juan", 70),
    Persona("María", 25),
    Persona("Pedro", 30),
    Persona("Antonio", 45),
    Persona("Laura", 22),
]

print("=" * 60)
print("LISTA DE PERSONAS Y SUS OBJETOS")
print("=" * 60)
for persona in personas:
    print(persona)

# --- Persona con el objeto más pesado ---
persona_objeto_mas_pesado = max(personas, key=lambda p: p.peso_maximo_objeto())

print("\n" + "=" * 60)
print("PERSONA CON EL OBJETO MÁS PESADO")
print("=" * 60)
objeto_mas_pesado = max(persona_objeto_mas_pesado.objetos, key=lambda o: o.peso)
print(f"{persona_objeto_mas_pesado.nombre} -> objeto más pesado: {objeto_mas_pesado}")

# --- Persona con más objetos ---
persona_mas_objetos = max(personas, key=lambda p: p.cantidad_objetos())

print("\n" + "=" * 60)
print("PERSONA CON MÁS OBJETOS")
print("=" * 60)
print(f"{persona_mas_objetos.nombre} -> {persona_mas_objetos.cantidad_objetos()} objetos")

# --- Ranking completo por objeto más pesado ---
print("\n" + "=" * 60)
print("RANKING POR OBJETO MÁS PESADO (de mayor a menor)")
print("=" * 60)
ordenadas_por_peso = sorted(personas, key=lambda p: p.peso_maximo_objeto(), reverse=True)
for persona in ordenadas_por_peso:
    print(f"{persona.nombre} -> peso máximo: {persona.peso_maximo_objeto()} kg")

# --- Ranking completo por cantidad de objetos ---
print("\n" + "=" * 60)
print("RANKING POR CANTIDAD DE OBJETOS (de mayor a menor)")
print("=" * 60)
ordenadas_por_cantidad = sorted(personas, key=lambda p: p.cantidad_objetos(), reverse=True)
for persona in ordenadas_por_cantidad:
    print(f"{persona.nombre} -> {persona.cantidad_objetos()} objetos")
