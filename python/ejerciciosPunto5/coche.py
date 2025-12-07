class coche:
    def __init__(self, marca, modelo, color, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.kilometraje = kilometraje
    def encender (self):
        print("El coche está encendido")
    def apagar (self):
        print ("El coche esta apagado")
    def conducir (self, kilometros):
        self.kilometraje = self.kilometraje+kilometros
    def detalles (self):
        print(f"{self.marca}, modelo {self.modelo}, de color {self.color}, y con {self.kilometraje} km")
c1 = coche("bmw", "m4", "negro", 290000)
c1.encender()
c1.apagar()
c1.detalles()
c1.conducir(1000)
c1.detalles()