import datetime

def mostrarFecha():
    fechaHoy=datetime.datetime.now()
    print(fechaHoy)

def numEntreFechas():
    fecha1_str = input("Introduce la fecha 1 en formato dd-mm-yyyy: ")
    fecha2_str = input("Introduce la fecha 2 en formato dd-mm-yyyy: ")


    fecha1 = datetime.datetime.strptime(fecha1_str, "%d-%m-%Y")
    fecha2 = datetime.datetime.strptime(fecha2_str, "%d-%m-%Y")
    diferencia = (fecha2 - fecha1).days
    print(f"Número de días entre las fechas: {diferencia}")
mostrarFecha()
numEntreFechas()