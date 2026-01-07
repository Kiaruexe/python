#Crea una clase Empleado con atributos nombre, puesto y salario. Luego, crea
#una subclase Gerente que añada un atributo departamento y un método
#informar.

class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario
class Gerente(Empleado):
    def __init__(self, nombre, puesto, salario, departamento):
        super().__init__(nombre, puesto, salario)
        self.departamento = departamento

    def informar(self):
        print(f"Gerente: {self.nombre}, Puesto: {self.puesto}, Salario: {self.salario}, Departamento: {self.departamento}")
        
# Ejemplo
gerente1 = Gerente("Carlos", "Gerente de Ventas", 75000, "Ventas")
gerente1.informar()
gerente2 = Gerente("Marta", "Gerente de Marketing", 80000, "Marketing")
gerente2.informar()