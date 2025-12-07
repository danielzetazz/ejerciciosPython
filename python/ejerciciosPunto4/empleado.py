class empleado:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario
    def aumento_salario(self, porcentaje):
        self.salario= self.salario * ((porcentaje/100)+1)
    
e1= empleado("daniel", "programador", 1500)
e1.aumento_salario(20)
print(e1.salario)
