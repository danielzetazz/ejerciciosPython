import json

sujeto = input("Dime el nombre: ")
tiempo = input("Dime la edad: ")
sitio = input("Dime la ciudad: ")

perfil = {
    "nombre": sujeto,
    "edad": tiempo,
    "ciudad": sitio
}

with open("usuario.json", "w", encoding="utf-8") as file:
    json.dump(perfil, file, indent=2, ensure_ascii=False)