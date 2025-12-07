class libro:
    def __init__ (self, titulo, autor, anio_publicacion, precio):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.precio= precio
    def mostrarInfo(self):
        print(f"El libro {self.titulo} de {self.autor} salió en: {self.anio_publicacion} y cuesta {self.precio}")
    def descuento(self, porcentaje):
        self.precio= self.precio- (self.precio * (porcentaje/100))


l1 = libro("test", "ojala yo", 2024, 15)
l1.mostrarInfo()
l1.descuento(10)
l1.mostrarInfo()