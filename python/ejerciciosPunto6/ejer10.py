
try:
    with open("datos.txt", "r", encoding="utf-8") as fuente:
        data_leida = fuente.read()
except FileNotFoundError:
    print("El fichero especificado no fue encontrado.")
except Exception as error_general:
    print("Ocurrió un fallo general al intentar leer el fichero.")

print(data_leida)