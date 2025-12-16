class Vehiculo:
    
    def __init__(self, marca, modelo, anio):
        self.marca=marca
        self.modelo=modelo
        self.anio=anio

    def describir(self):
        return f"{self.marca} - {self.modelo} - Año: {self.anio}"

class Auto (Vehiculo):

    def __init__(self, marca, modelo, anio, num_puertas):
        super().__init__(marca, modelo, anio)
        self.num_puertas=num_puertas

    def describir(self):
        return f"{self.marca} - {self.modelo} - Puertas: {self.num_puertas} - Año: {self.anio}"
    
    def to_dict(self):
        return     {
        "tipo": "auto",
        "marca": self.marca,
        "modelo": self.modelo,
        "anio": self.anio,
        "num_puertas": self.num_puertas
        }
class Motocicleta (Vehiculo):

    def __init__(self, marca, modelo, anio, cilindraje):
        super().__init__(marca, modelo, anio)
        self.cilindraje=cilindraje

    def describir(self):
        return f"{self.marca} - {self.modelo} - CC: {self.cilindraje} - Año: {self.anio}"
    
    def to_dict(self):
        return     {
        "tipo": "moto",
        "marca": self.marca,
        "modelo": self.modelo,
        "anio": self.anio,
        "cilindraje": self.cilindraje
        }
