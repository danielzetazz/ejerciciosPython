import csv

archivo_csv = "productos.csv"

with open(archivo_csv, "r", encoding="utf-8") as data:
    lector_csv = csv.reader(data)
    
    next(lector_csv)
    
    cuenta = 0
    for elemento in lector_csv:
        cuenta = cuenta + 1

print(f"Cantidad de filas encontradas: {cuenta}")