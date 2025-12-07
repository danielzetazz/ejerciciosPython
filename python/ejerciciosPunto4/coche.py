class coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    def encender (self):
        print("El coche está encendido")
    def apagar (self):
        print ("El coche esta apagado")
c1 = coche("bmw", "m4", "negro")
c1.encender()
c1.apagar()