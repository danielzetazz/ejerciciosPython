from cliente import Cliente
import json

listaClientes=[]
def cargarClientes():
    with open("clientes.json", "r", encoding="utf-8") as archivo:
        contenido= json.load(archivo)
        for usuario in contenido:
            listaClientes.append(Cliente(usuario["nombre"], usuario["email"], usuario["ciudad"], usuario["telefono"], usuario["pedidos"]))

cargarClientes()

def guardarClientes():
    lista_json = [c.to_dict() for c in listaClientes] #Mete en una lista de strings el json de cada cliente
    with open("clientes.json", "w", encoding="utf-8") as archivo:
        escritor=json.dump(lista_json, archivo, indent=5, ensure_ascii=False)
        
def guardarClientesPremium(clientesPremium):
    with open ("clientes_premium.txt", "w", encoding="utf-8") as archivo:
        for cliente in clientesPremium:
            archivo.write(f"{cliente.nombre}, pedidos: {cliente.pedidos_realizados}")
keepAlive = True

def mostrarClientes():
    for cliente in listaClientes:
        print(f"{cliente.__str__()}")

def introducirCliente():
    nombre = input("Introduce el nombre: ")
    email = input("Introduce el email: ")
    ciudad = input("Introduce la ciudad: ")
    telefono = input("Introduce el telefono: ")
    pedidos = input("Introduce los pedidos realizados(formato XX-XX-XX): ")
    try:

        clienteNuevo=Cliente(nombre, email, ciudad, telefono, pedidos)
        listaClientes.append(clienteNuevo)
        guardarClientes()

    except ValueError as e:

        print(f"Valores incorrectos: {e}")



def buscarPorEmail(email):
    for cliente in listaClientes:
        if cliente.email == email: print(f"{cliente.__str__()}, pedidos ordenados: {cliente.ordenarPedidos()}")

def guardarPremium():
    clientesPremium=[]
    for cliente in listaClientes:
        pedidos=cliente.ordenarPedidos()
        money=0
        for pedido in pedidos:
            money+=pedido
        if money>500: clientesPremium.append(cliente)
    guardarClientesPremium(clientesPremium)


while (keepAlive):
    print("1.- Mostrar listado de clientes \n2.- Introducir nuevo cliente\n3.- Buscar por email\n4.- Guardar clientes Premium\n5.- Salir")
    respuesta= input("Introduce una opción: ")
    match respuesta:
        case "1" :
            mostrarClientes()
        case "2": 
            introducirCliente()
        case "3" :
            email= input("Introduce el email a buscar: ")
            buscarPorEmail(email)
        case "4": 
            guardarPremium()
        case "5" :
            keepAlive=False
        case "_": 
            keepAlive=False
