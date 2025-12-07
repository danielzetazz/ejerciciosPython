class persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def saludar (self):
        print(f"{self.nombre} saluda")
    
p1 = persona("daniel",18,"español")
p1.saludar()