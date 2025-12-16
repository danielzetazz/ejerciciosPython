import csv

ruta = "estudiantes.csv"

with open(ruta, "w", encoding="utf-8", newline="") as f:
    pluma = csv.writer(f)

    cabecera = ["Nombre", "Edad", "Curso"]
    pluma.writerow(cabecera)
    
    pluma.writerow(["Ana", 20, "Matemáticas"])
    pluma.writerow(["Pedro", 22, "Física"])
    pluma.writerow(["María", 21, "Química"])