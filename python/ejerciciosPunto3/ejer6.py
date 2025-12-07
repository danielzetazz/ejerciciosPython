import math
def raizCuadrada():
    x = float(input("Introduzca un numero para calcular su raiz cuadrada: "))
    print("La raiz es: ", math.sqrt(x))
def valorDePi():
    r = float(input("Introduzca el radio: "))
    area = math.pi * (r ** 2)
    print("El área es:", area)
raizCuadrada()
valorDePi()