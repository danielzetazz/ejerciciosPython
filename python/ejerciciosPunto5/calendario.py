class calendario:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes =mes
        self.año =año
    def fecha_completa (self):
        return f"{self.dia}-{self.mes}-{self.año}"
    def es_bisiesto(self):
        return (self.año % 4 == 0 and self.año % 100 != 0) or (self.año % 400 == 0)
c1= calendario(27,12,2016)
print(c1.fecha_completa())
print(c1.es_bisiesto())