import csv

documento = "productos.csv"

with open(documento, "r", encoding="utf-8") as f:
    contenido = csv.reader(f)
    
    next(contenido) 
    
    total = 0
    for fila in contenido:
        total += 1

print(f"Número de registros: {total}")