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
        print("guau ")
p1 = perro("Toby", "pug")
p1.hablar()