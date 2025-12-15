with open("texto.txt", "r", encoding="utf-8") as fuente_datos:
    texto_leido = fuente_datos.read()   
    contador_unidades = len(texto_leido.split(" "))
    
print(contador_unidades)

print(texto_leido)