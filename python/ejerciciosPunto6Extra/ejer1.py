import csv

path = "productos.csv"

with open(path, "r", encoding="utf-8") as f:
    datos = csv.reader(f)
    
    for fila in datos:
        print(fila)