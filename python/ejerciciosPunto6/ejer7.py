termino_busqueda = input("Ingresa el término que deseas contar: ")

with open("texto.txt", "r", encoding="utf-8") as recurso_lectura:
    cadena_completa = recurso_lectura.read()
    frecuencia = cadena_completa.count(termino_busqueda)

print(f"La palabra aparece {frecuencia} veces")