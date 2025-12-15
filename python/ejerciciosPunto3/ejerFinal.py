class Empleado:
    def __init__(self, nombre, edad, departamento):
        self.nombre=nombre
        self.edad=edad
        self.departamento=departamento
        
    def mostrarInformacion(self):
        print(f"{self.nombre}, edad: {self.edad} años, departamento: {self.departamento}")
    def to_dict(self):
        return {
            "tipo": "Empleado",
            "nombre": self.nombre,
            "edad": self.edad,
            "departamento": self.departamento
        }
    
class Gerente(Empleado):
    def __init__(self, nombre, edad, departamento, equipo):
        super().__init__(nombre, edad, departamento)
        self.equipo=equipo
    def mostrarInformacion(self):
        print(f"{self.nombre}, edad: {self.edad} años, departamento: {self.departamento}, equipo: {self.equipo}")
    def to_dict(self):
        return {
            "tipo": "Gerente",
            "nombre": self.nombre,
            "edad": self.edad,
            "departamento": self.departamento,
            "equipo": self.equipo
        }

class Desarrollador(Empleado):
    def __init__(self, nombre, edad : int, departamento, lenguaje_programacion):
        super().__init__(nombre, edad, departamento)
        self.lenguaje_programacion=lenguaje_programacion
    def mostrarInformacion(self):
        print(f"{self.nombre}, edad: {self.edad} años, departamento: {self.departamento}, lenguaje: {self.lenguaje_programacion}")
    def to_dict(self):
        return {
            "tipo": "Desarrollador",
            "nombre": self.nombre,
            "edad": self.edad,
            "departamento": self.departamento,
            "lenguaje_programacion": self.lenguaje_programacion
        }

import os
import json
with open("empleados.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo) 

listaEmpleados= list()
for empleado in datos:
    if (empleado['tipo'] == "Empleado"):
        empleadoNuevo = Empleado(empleado['nombre'], empleado['edad'], empleado['departamento'])
        listaEmpleados.append(empleadoNuevo)
    if (empleado['tipo'] == "Gerente"):
        empleadoNuevo = Gerente(empleado['nombre'], empleado['edad'], empleado['departamento'], empleado['equipo'])
        listaEmpleados.append(empleadoNuevo)
    if (empleado['tipo'] == "Desarrollador"):
        empleadoNuevo = Desarrollador(empleado['nombre'], empleado['edad'], empleado['departamento'], empleado['lenguaje_programacion'])
        listaEmpleados.append(empleadoNuevo)

for e in listaEmpleados:
    e.mostrarInformacion()

nuevo_gerente = Gerente("Lucía", 40, "Dirección", "Equipo de Marketing")
listaEmpleados.append(nuevo_gerente)

datos_guardar = [emp.to_dict() for emp in listaEmpleados]
with open("empleados.json", "w", encoding="utf-8") as archivo:
    json.dump(datos_guardar, archivo, indent=4, ensure_ascii=False)



