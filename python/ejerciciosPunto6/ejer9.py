import csv

nombre_documento = "usuarios_info.csv"

with open(nombre_documento, "w", newline="") as fichero:
    grabador = csv.writer(fichero)
    
    grabador.writerow(["DatoA", "DatoB"])
    grabador.writerow(["Pedro", 29])
    grabador.writerow(["Julia", 35])
    grabador.writerow(["Marcos", 41])

with open(nombre_documento, "r") as fuente:
    lector_datos = csv.reader(fuente)
    
    for registro in lector_datos:
        print(f"Registro: {registro[0]} - Número: {registro[1]}")