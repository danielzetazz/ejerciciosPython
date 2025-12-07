class estudiante:
    def __init__(self, nombre, nota1, nota2, nota3):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 =nota2
        self.nota3 = nota3
    def calcularPromedio(self):
        return (self.nota1+self.nota2+self.nota3)/3
    def aprobado(self):
        if self.calcularPromedio()>5:
            return True
        else:
            return False
    def informacion(self):
        if self.aprobado():
            print (f"El estudiante: {self.nombre},  ha aprobado")
        else:
            print (f"El estudiante: {self.nombre}, ha suspendido")
        
        

e1 = estudiante("Daniel",7,9,6)
e1.informacion()
        