import json

valor = input("Introduce el nombre de la tarea: ")

with open("tareas.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

datos["lista_actividades"].append(valor)

with open("tareas.json", "w", encoding="utf-8") as archivo:
    json.dump(datos, archivo, indent=2, ensure_ascii=False)