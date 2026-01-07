#Modifica la clase Animal para que cada subclase (Perro, Gato) tenga un
#método hacer_sonido que imprima un sonido diferente según el tipo de
#animal. Llama al método en un objeto de cada clase.

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
class Perro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Guau Guau!")
        
class Gato(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Miau Miau!")
        
# Ejemplo
perro1 = Perro("Rex", 3)
perro1.hacer_sonido()
gato1 = Gato("Misu", 2)
gato1.hacer_sonido()
