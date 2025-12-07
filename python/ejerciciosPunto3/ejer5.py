class vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    def detalles (self):
        print(f"{self.marca}, modelo {self.modelo}, de color {self.color}")

class coche (vehiculo):
    def __init__(self, marca, modelo, color, numero_puertas):
        super().__init__(marca, modelo, color)
        self.numero_puertas=numero_puertas
    def detalles(self):
        print(f"{self.marca}, modelo {self.modelo}, de color {self.color}, con {self.numero_puertas} puertas")
class motocicleta (vehiculo):
    def __init__(self, marca, modelo, color, numero_ruedas):
        super().__init__(marca, modelo, color)
        self.numero_ruedas=numero_ruedas
    def detalles(self):
        print(f"{self.marca}, modelo {self.modelo}, de color {self.color}, con {self.numero_ruedas} ruedas")
    
def mostrarInformacion(vehiculo: vehiculo):
    vehiculo.detalles()

v1 = vehiculo("bmw", "m4", "negro")
c1 = coche("bmw", "m4", "negro", 4)
m1 = motocicleta("bmw", "m4", "negro", 2)

mostrarInformacion(c1)
mostrarInformacion(m1)