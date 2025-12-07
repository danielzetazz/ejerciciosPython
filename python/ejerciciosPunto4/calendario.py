class calendario:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes =mes
        self.año =año
    def fecha_completa (self):
        return f"{self.dia}-{self.mes}-{self.año}"
    
c1= calendario(27,12,2030)
print(c1.fecha_completa())