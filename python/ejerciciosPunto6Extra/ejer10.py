import json
import csv

with open("datos.json", "r", encoding="utf-8") as f:
    info = json.load(f)

with open("datos_convertidos.csv", "w", encoding="utf-8", newline="") as salida:
    cabecera = ["nombre", "edad", "ciudad"]
    
    escritor = csv.DictWriter(salida, fieldnames=cabecera)
    escritor.writeheader()

    for registro in info:
        escritor.writerow(registro)