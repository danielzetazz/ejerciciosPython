class telefono:
    def __init__(self, marca, modelo, numero):
        self.marca = marca
        self.modelo =modelo
        self.numero =numero
    def hacer_llamada(self):
        print (f"Realizando llamada a {self.numero}")
    def enviar_mensaje(self):
        print (f"Enviando mensaje a {self.numero}")
    def detalles(self):
        print (f"{self.modelo}, de {self.marca}, con numero: {self.numero}")
t1 = telefono("Apple", "Iphone 17", "234878374")
t1.detalles()
t1.hacer_llamada()
t1.enviar_mensaje()