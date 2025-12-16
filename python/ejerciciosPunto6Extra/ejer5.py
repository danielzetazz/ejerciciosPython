import csv

user = input("Nombre del estudiante: ")
years = input("Edad del estudiante: ")
clase = input("Grado del estudiante: ")

with open("estudiantes.csv", "a", encoding="utf-8", newline="") as f:
    grabador = csv.writer(f)
    
    grabador.writerow([user, years, clase])