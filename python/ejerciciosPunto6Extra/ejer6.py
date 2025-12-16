import json

with open("datos.json", "r", encoding="utf-8") as f:
    contenido = json.load(f)

print(contenido)