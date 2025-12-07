class empleado:
    def __init__(self, nombre, puesto, salario, antiguedad):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario
        self.antiguedad = antiguedad
    def aumento_salario(self, porcentaje):
        self.salario=int(self.salario * ((porcentaje/100)+1))
    def mostrar_informacion (self):
        print (f"{self.nombre} es {self.puesto}, cobra {self.salario}, y lleva {self.antiguedad} año/s")
    
e1= empleado("daniel", "programador", 1500, 1)
e1.mostrar_informacion()
e1.aumento_salario(20)
e1.mostrar_informacion()
