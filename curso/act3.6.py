#Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una 
# nueva clase CuentaJoven que deriva de la anterior. Cuando se crea esta 
# nueva clase, además del titular y la cantidad se debe guardar una 
# bonificación que estará expresada en tanto por ciento.Construye los 
# siguientes métodos para la clase:

#Un constructor.
#Los setters y getters para el nuevo atributo.
#En esta ocasión los titulares de este tipo de cuenta tienen que ser 
# mayor de edad., por lo tanto hay que crear un método esTitularValido() 
# que devuelve verdadero si el titular es mayor de edad pero menor de 
# 25 años y falso en caso contrario.
#Además la retirada de dinero sólo se podrá hacer si el titular es válido.
#El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la 
# bonificación de la cuenta.
#Piensa los métodos heredados de la clase madre que hay que reescribir.
from act25 import Cuenta
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion

    def get_bonificacion(self):
        return self.bonificacion

    def esTitularValido(self):
        edad = self.titular.get_edad()
        return 18 <= edad < 25

    def retirar(self, cantidad):
        if self.esTitularValido():
            super().retirar(cantidad)
        else:
            print("Retirada no permitida: Titular no válido.")

    def mostrar(self):
        print(f"Cuenta Joven - Bonificación: {self.bonificacion}%")
        super().mostrar()
        
#Ejemplo de uso
from act113 import Persona
titular_joven = Persona("Luis Martínez", 22, "87654321X")
cuenta_joven = CuentaJoven(titular_joven, 200.0, 5.0)
cuenta_joven.mostrar()
cuenta_joven.retirar(50.0)
cuenta_joven.mostrar()
titular_no_valido = Persona("Ana López", 30, "12345678Z")
cuenta_no_valida = CuentaJoven(titular_no_valido, 300.0, 3.0)
cuenta_no_valida.mostrar()
cuenta_no_valida.retirar(50.0)
cuenta_no_valida.mostrar()

