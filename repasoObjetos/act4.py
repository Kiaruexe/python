#Crea una clase Estudiante con los atributos nombre, edad y nota_media.
#Añade un método que imprima si el estudiante ha aprobado o suspendido
#según su nota_media.

class Estudiante:
    def __init__(self, nombre, edad, nota_media):
        self.nombre = nombre
        self.edad = edad
        self.nota_media = nota_media

    def estado_aprobacion(self):
        if self.nota_media >= 5:
            print(f"{self.nombre} ha aprobado con una nota media de {self.nota_media}.")
        else:
            print(f"{self.nombre} ha suspendido con una nota media de {self.nota_media}.")

# Ejemplo
estudiante1 = Estudiante("Ana", 20, 7.5)
estudiante1.estado_aprobacion()
estudiante2 = Estudiante("Luis", 22, 4.3)
estudiante2.estado_aprobacion()
