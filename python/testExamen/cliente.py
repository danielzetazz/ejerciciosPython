class Cliente:
    def __init__(self, nombre, email, ciudad, telefono, pedidos_realizados):
        self.nombre=nombre
        self.email=email
        self.ciudad=ciudad
        self.telefono=telefono
        self.pedidos_realizados=pedidos_realizados

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
    

