class rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area (self):
        x = self.base*self.altura
        return x

r1 = rectangulo(7,9)
print(r1.area())