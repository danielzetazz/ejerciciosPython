class animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
    def hablar (self) :
        print(f"{self.nombre} está hablando")

class perro (animal):
    def __init__(self, nombre, especie):
        super().__init__(nombre, especie)
    def hablar(self):        
        print("guau")
class gato (animal):
    def __init__(self, nombre, especie):
        super().__init__(nombre, especie)
    def hablar(self):        
        print("miau")
p1 = perro("Toby", "pug")
p1.hablar()
c1 = gato("Luna", "blanco")
c1.hablar()