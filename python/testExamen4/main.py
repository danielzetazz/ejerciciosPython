from modelo_concesionario import Turismo
from modelo_concesionario import Furgoneta

listaVehiculos = []

import json
import csv

def cargarDatos():
    with open("vehiculos_ocasion.json", "r", encoding="utf-8") as archivo:
        lector = json.load(archivo)
        for l in lector:
            match l["tipo"]:
                case "turismo": listaVehiculos.append(Turismo(l["marca"], l["modelo"], l["precio"], l["kilometraje"] ))
                case "furgoneta": listaVehiculos.append(Furgoneta(l["marca"], l["modelo"], l["precio"], l["capacidad_carga"] ))

def escribirDatos():
    listaJson = []
    for v in listaVehiculos:
        listaJson.append(v.to_dict())
    with open("vehiculos_ocasion.json", "w", encoding="utf-8") as archivo:
        escritor = json.dump(listaJson, archivo, ensure_ascii=False, indent=5)

cargarDatos()

def filtrarPresupuesto(presupuesto):
    listraFiltrado = []
    for v in listaVehiculos:
        if v.precio <= presupuesto: listraFiltrado.append(v)
    for l in listraFiltrado:
        print(l.mostrar_info())

filtrarPresupuesto(14000)

def exportarCsv():
    test = []
    for v in listaVehiculos:
        if isinstance(v, Furgoneta): test.append(v.to_dict2())
    cabeceras=["marca", "modelo", "precio", "capacidad_carga"]
    with open("furgonetas_stock.csv", "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=cabeceras)
        escritor.writeheader()
        for t in test:
            escritor.writerow(t)
exportarCsv()