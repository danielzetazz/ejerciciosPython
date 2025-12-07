class rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area (self):
        x = self.base*self.altura
        return x
    def perimetro(self):
        x = self.base*2+self.altura*2
        return x
    def es_cuadrado(self):
        if (self.base==self.altura):
            return True
        else: return False
        
r1 = rectangulo(9,9)
print(r1.area())
print(r1.perimetro())
print(r1.es_cuadrado())