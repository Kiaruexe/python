#Crea una clase Empleado con un método calcular_bonus que calcule el bono
#anual de un empleado. Luego, crea una subclase Vendedor que modifique el
#método para calcular el bono según las ventas realizadas.

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_bonus(self):
        bonus = self.salario * 0.10  # 10% del salario como bono
        return bonus
    
class Vendedor(Empleado):
    def __init__(self, nombre, salario, ventas_realizadas):
        super().__init__(nombre, salario)
        self.ventas_realizadas = ventas_realizadas

    def calcular_bonus(self):
        bonus_base = super().calcular_bonus()
        bonus_ventas = self.ventas_realizadas * 0.05  # 5% de las ventas como bono adicional
        return bonus_base + bonus_ventas
# Ejemplo
empleado1 = Empleado("Laura", 50000)
print(f"El bono anual de {empleado1.nombre} es: {empleado1.calcular_bonus()}")
vendedor1 = Vendedor("Pedro", 40000, 200000)
print(f"El bono anual de {vendedor1.nombre} es: {vendedor1.calcular_bonus()}")
vendedor2 = Vendedor("Sofía", 45000, 150000)
print(f"El bono anual de {vendedor2.nombre} es: {vendedor2.calcular_bonus()}")
