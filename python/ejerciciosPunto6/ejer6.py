import shutil as fs_util

fs_util.copy("datos.txt", "respaldo.txt")

with open("respaldo.txt", "r", encoding="utf-8") as flujo_acceso:
    contenido_fichero = flujo_acceso.read()

print(contenido_fichero)