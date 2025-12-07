class libro:
    def __init__ (self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
    def mostrarInfo(self):
        print(f"El libro {self.titulo} de {self.autor} salió en: {self.anio_publicacion}")

l1 = libro("test", "ojala yo", 2024)
l1.mostrarInfo()