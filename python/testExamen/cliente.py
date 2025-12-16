class Cliente:
    def __init__(self, nombre, email, ciudad, telefono, pedidos_realizados):
        self.nombre=nombre
        self.email=email
        self.ciudad=ciudad
        self.telefono=telefono
        self.pedidos_realizados=pedidos_realizados

    @property
    def nombre(self):
        return self.__nombre
    @property
    def email(self):
        return self.__email
    @property
    def ciudad(self):
        return self.__ciudad
    @property
    def telefono(self):
        return self.__telefono
    @property
    def pedidos_realizados(self):
        return self.__pedidos_realizados

    @nombre.setter
    def nombre(self, nuevoNombre):
        if not nuevoNombre:
            raise ValueError("El nombre no puede estar vacío")
        self.__nombre = nuevoNombre


    @email.setter
    def email(self, nuevoemail):
        if "@" not in nuevoemail:
            raise ValueError("El email no contiene @")
        self.__email = nuevoemail


    @ciudad.setter
    def ciudad(self, nuevaCiudad):
        self.__ciudad = nuevaCiudad


    @telefono.setter
    def telefono(self, valor):
        if not valor.isdigit():
            raise ValueError("El teléfono debe ser numérico")
        self.__telefono = valor


    @pedidos_realizados.setter
    def pedidos_realizados(self, valor):
        if not all(p.isdigit() for p in valor.split("-")):
            raise ValueError("Formato inválido (ej: 29-39-40)")
        self.__pedidos_realizados = valor

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "email": self.email,
            "ciudad": self.ciudad,
            "telefono": self.telefono,
            "pedidos": self.pedidos_realizados  
        }
    
    def __str__(self):
        return f"{self.nombre} - {self.email} - {self.ciudad} - {self.telefono} - {self.pedidos_realizados}"

    def ordenarPedidos (self):
        pedidosCadena= list(map(int, self.pedidos_realizados.split("-")))
        return sorted(pedidosCadena, reverse=True)
    

