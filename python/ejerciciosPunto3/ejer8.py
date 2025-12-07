import random

def tirarDado():
    dado = random.randint(1,6)
    print(dado)
def lista():
    lista = list()
    for i in range(10):
        lista.append(random.randint(1,100))
    lista.sort()
    print(lista)
tirarDado()
lista()
