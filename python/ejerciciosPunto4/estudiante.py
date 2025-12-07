class estudiante:
    def __init__(self, nombre, curso, nota_final):
        self.nombre = nombre
        self.curso = curso
        self.nota_final = nota_final
    def aprobar (self):
        if self.nota_final>=5:
            print(f"{self.nombre} ha aprobado")
        else:
            print(f"{self.nombre} ha suspendido")

e1 = estudiante("Daniel", "ERP", 7)
e1.aprobar()
        