from biblioteca_modelo import Libro
from biblioteca_modelo import Revista
import json
import csv


listaMaterial = []

def cargarDatos():
    with open("libros.json", "r", encoding="utf-8") as archivo:
        contenido=json.load(archivo)
        for m in contenido:
            match m["tipo"]:
                case "revista": listaMaterial.append(Revista(m["titulo"], m["autor"], m["anio"], m["numero_edicion"]))
                case "libro": listaMaterial.append(Libro(m["titulo"], m["autor"], m["anio"], m["genero"]))
def escribirDatos():
    escribir= []
    for m in listaMaterial:
        escribir.append(m.to_dict())
    with open("libros.json", "w", encoding="utf-8") as archivo:
        escritor = json.dump(escribir, archivo, ensure_ascii=False, indent=5)
cargarDatos()

def agregarLibro():
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    anio = int(input("Anio: "))
    genero = input("genero: ")
    try:
            libro = Libro(titulo, autor, anio, genero)
            listaMaterial.append(libro)
        
    except ValueError as er: print(er)

def agregarRevista():
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    anio = input("Anio: ")
    numero_edicion = input("Numero_edicion: ")
    revista = Revista(titulo, autor, anio, numero_edicion)
    listaMaterial.append(revista)
def buscarPorAutor(autor):
    for m in listaMaterial:
        if autor in m.autor:
            print(m.describir())
def exportCsv():
    cabeceras= ["titulo", "autor", "anio", "genero"]
    with open("biblioteca.csv", "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=cabeceras)
        escritor.writeheader()
        for m in listaMaterial:
            if isinstance(m, Libro):escritor.writerow(m.to_dict2())

    leerCsv()
            
def leerCsv():
    with open("biblioteca.csv", "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        for row in lector:
            print(row)
            
keepAlive = True
while keepAlive :

    print ("1.- Agregar libro\n2.- Agregar revista\n3.- Buscar por autor\n4.- Export a CSV\n5.- Guardar y salir")
    respuesta = input ("Introduce una opción: ")
    for m in listaMaterial:
        print(m.describir())
    match respuesta:
        case "1":
            agregarLibro()
        case "2":
            agregarRevista()
        case "3":
            autor = input("Introduce el nombre del autor: ")
            buscarPorAutor(autor)
        case "4":
            exportCsv()
        case _:
            escribirDatos()
            keepAlive= False

