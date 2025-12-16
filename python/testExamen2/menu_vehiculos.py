from vehiculo import Vehiculo
from vehiculo import Auto
from vehiculo import Motocicleta
import json

listaVehiculos = []

def cargarVehiculos():
    with open ("vehiculos.json", "r", encoding="utf-8") as archivo:
        contenido=json.load(archivo)
        for linea in contenido:
            match linea["tipo"]:
                
                case "auto":
                    listaVehiculos.append(Auto(linea["marca"], linea["modelo"], linea["anio"], linea["num_puertas"]))
                case "motocicleta":
                    listaVehiculos.append(Motocicleta(linea["marca"], linea["modelo"], linea["anio"], linea["cilindraje"]))
cargarVehiculos()

def guardarVehiculos():
    diccionarioJson=[]
    for v in listaVehiculos:
        diccionarioJson.append(v.to_dict())
    with open ("vehiculos.json", "w", encoding="utf-8") as archivo:
        escritor=json.dump(diccionarioJson, archivo, ensure_ascii=False, indent=5)

def introducirAuto():
    marca=input("Introduce la marca: ")
    modelo=input("Introduce el modelo: ")
    anio=input("Introduce el año: ")
    num_puertas=input("Introduce el numero de puertas: ")
    listaVehiculos.append(Auto(marca, modelo, anio, num_puertas))

def introducirMoto():
    marca=input("Introduce la marca: ")
    modelo=input("Introduce el modelo: ")
    anio=input("Introduce el año: ")
    cilindrada=input("Introduce la cilindrada: ")
    listaVehiculos.append(Motocicleta(marca, modelo, anio, cilindrada))

def mostrarVehiculos():
    for v in listaVehiculos:
        print(v.describir())
keepAlive = True

def guardarYSalir():
    guardarVehiculos()

import csv
def guardarAutosCsv():
    with open("autos.csv", "w", encoding="utf-8") as archivo:
        cabeceras=["tipo", "marca", "modelo", "anio", "num_puertas"]
        autos = []
        for v in listaVehiculos:
            if isinstance(v, Auto):
                autos.append(v.to_dict())
        escritor = csv.DictWriter(archivo, fieldnames=cabeceras)
        escritor.writeheader()
        print(autos)
        for a in autos:
           escritor.writerow(a)
        
def mostrarAutosCsv():
    with open ("autos.csv", "r", encoding="utf-8") as archivo:
        lector= csv.reader(archivo)
        for l in lector:
            print(l)
            
while keepAlive:
    print("1. Agregar un auto\n2. Agregar una motocicleta\n3. Mostrar todos los vehiculos\n4. Guardar y salir\n5. Escribirlo en csv\n6. Mostrar csv")
    respuesta = input("Introduce una opción:")
    match respuesta:
        case "1": introducirAuto()
        case "2": introducirMoto()
        case "3": mostrarVehiculos()
        case "4": 
            guardarYSalir()
            keepAlive=False
        case "5": 
            guardarAutosCsv()
        case "6": 
            mostrarAutosCsv()
        case "_": print("Introduce una opción correcta")
