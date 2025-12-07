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
    def reducirStock(self, cantidad):
        if (self.stock-cantidad)>=0:
            self.stock = self.stock-cantidad
        else:
            print (f"Cantidad superior al stock actual. Stock actual: {self.stock}")
    def actualizarPrecio (self, precio):
        self.precio=precio
    

p1 = producto("test", 20,10)
p1.disponibilidad()
p1.actualizarPrecio(25)
print(p1.precio)
p1.reducirStock(15)
p1.reducirStock(7)
print(p1.stock)