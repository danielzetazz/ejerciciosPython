import json

item = input("Nombre de la nueva labor: ")

with open("tareas.json", "r", encoding="utf-8") as archivo:
    data = json.load(archivo)

if "lista_actividades" not in data:
    data["lista_actividades"] = []

data["lista_actividades"].append(item)

with open("tareas.json", "w", encoding="utf-8") as archivo:
    json.dump(data, archivo, indent=4, ensure_ascii=False)