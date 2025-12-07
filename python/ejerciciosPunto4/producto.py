class producto:
    def __init__ (self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    def disponibilidad(self):
        if self.stock>0:
            print("Hay stock")
        else:
            print ("No hay stock")
p1 = producto("test", 20,10)
p1.disponibilidad()