#Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular 
# (que es una persona) y cantidad (puede tener decimales). El titular será 
# obligatorio y la cantidad es opcional. Construye los siguientes métodos 
# para la clase:

#Un constructor, donde los datos pueden estar vacíos.
#Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, solo ingresando o retirando dinero.
#mostrar(): Muestra los datos de la cuenta.
#ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
#retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def set_titular(self, titular):
        self.titular = titular

    def get_titular(self):
        return self.titular

    def get_cantidad(self):
        return self.cantidad

    def mostrar(self):
        print(f"Titular: {self.titular}, Cantidad: {self.cantidad:.2f} euros")
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
    def retirar(self, cantidad):
        self.cantidad -= cantidad
#Ejemplo de uso
cuenta1 = Cuenta("Juan Pérez", 100.0)
cuenta1.mostrar()
cuenta1.ingresar(50.0)
cuenta1.mostrar()
cuenta1.retirar(30.0)
cuenta1.mostrar()
cuenta1.retirar(150.0)
cuenta1.mostrar()