class Material:
    def __init__(self, titulo, autor, anio):
        self.titulo=titulo
        self.autor=autor
        self.anio=anio

    @property
    def titulo(self):
        return self.__titulo
    @titulo.setter
    def titulo(self, valor):
        self.__titulo=valor
    @property
    def autor(self):
        return self.__autor
    @autor.setter
    def autor(self, valor):
        self.__autor=valor
    @property
    def anio(self):
        return self.__anio
    @anio.setter
    def anio(self, valor):
        import datetime
        if valor>datetime.date.today().year: 
            raise ValueError("Hola amego")
        self.__anio=valor

class Libro(Material):
    def __init__(self, titulo, autor, anio, genero):
        super().__init__(titulo, autor, anio)
        self.genero=genero
    @property
    def genero(self):
        return self.__genero
    @genero.setter
    def genero(self, valor):
        self.__genero=valor

    def describir(self):
        return f"{self.titulo} - {self.autor} - {self.anio} - {self.genero}"
    def to_dict(self):
        return  {   
                    "tipo": "libro",
                    "titulo": self.titulo,
                    "autor": self.autor,
                    "anio": self.anio,
                    "genero": self.genero
                }
    def to_dict2(self):
        return  {   
                    "titulo": self.titulo,
                    "autor": self.autor,
                    "anio": self.anio,
                    "genero": self.genero
                }

class Revista(Material):
    def __init__(self, titulo, autor, anio, numero_edicion):
        super().__init__(titulo, autor, anio)
        self.numero_edicion=numero_edicion
    @property
    def numero_edicion(self):
        return self.__numero_edicion
    @numero_edicion.setter
    def numero_edicion(self, valor):
        self.__numero_edicion=valor

    def describir(self):
        return f"{self.titulo} - {self.autor} - {self.anio} - {self.numero_edicion}"
    def to_dict(self):
        return  {
                    "tipo": "revista",
                    "titulo": self.titulo,
                    "autor": self.autor,
                    "anio": self.anio,
                    "numero_edicion": self.numero_edicion
                }
