#Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. 
# Construye los siguientes métodos para la clase:

#Un constructor, donde los datos pueden estar vacíos.
#Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
#mostrar(): Muestra los datos de la persona.
#esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
#el dni debe estar validado como dni español (8 números y una letra).
class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_edad(self, edad):
        if edad >= 0:
            self.edad = edad
        else:
            print("Edad no válida.")

    def get_edad(self):
        return self.edad

    def set_dni(self, dni):
        if self.validar_dni(dni):
            self.dni = dni
        else:
            print("DNI no válido.")

    def get_dni(self):
        return self.dni

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}")

    def esMayorDeEdad(self):
        return self.edad >= 18

    def validar_dni(self, dni):
        if len(dni) != 9:
            return False
        num_part = dni[:-1]
        letra_part = dni[-1].upper()
        if not num_part.isdigit():
            return False
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        letra_correcta = letras[int(num_part) % 23]
        return letra_part == letra_correcta
#Ejemplo de uso
persona = Persona()
persona.set_nombre("Ana García")
persona.set_edad(25)
persona.set_dni("12345678Z")
persona.mostrar()
print("¿Es mayor de edad?", persona.esMayorDeEdad())
persona.set_dni("12345678A")  # DNI no válido.
persona.mostrar()
