class Vehiculo:
    def __init__(self, marca, modelo, precio):
        self.marca=marca
        self.modelo=modelo
        self.precio=precio
    @property
    def precio(self):
        return self.__precio
    @precio.setter
    def precio(self, valor):
        if int(valor)>=0 : self.__precio=valor
        else: raise ValueError("El precio no puede ser negativo")
    
class Turismo (Vehiculo):
    def __init__(self, marca, modelo, precio, kilometraje):
        super().__init__(marca, modelo, precio)
        self.kilometraje=kilometraje
    def mostrar_info(self):
        return f"{self.marca} - {self.modelo} - {self.precio} - {self.kilometraje}"
    def to_dict(self):
        return     {
                        "tipo": "turismo",
                        "marca": self.marca,
                        "modelo": self.modelo,
                        "precio": self.precio,
                        "kilometraje": self.kilometraje 
                    }

class Furgoneta (Vehiculo):
    def __init__(self, marca, modelo, precio, capacidad_carga):
        super().__init__(marca, modelo, precio)
        self.capacidad_carga=capacidad_carga
    def mostrar_info(self):
        return f"{self.marca} - {self.modelo} - {self.precio} - {self.capacidad_carga}"
    
    def to_dict(self):
        return     {
                        "tipo": "furgoneta",
                        "marca": self.marca,
                        "modelo": self.modelo,
                        "precio": self.precio,
                        "capacidad_carga": self.capacidad_carga 
                    }
    def to_dict2(self):
        return     {
                        "marca": self.marca,
                        "modelo": self.modelo,
                        "precio": self.precio,
                        "capacidad_carga": self.capacidad_carga 
                    }
