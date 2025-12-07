import os

def crearNuevaCarpeta():
    os.mkdir("test")
def listarTodo():
    x = os.listdir()
    for e in x:
        print (e)
crearNuevaCarpeta()
listarTodo()