class cuentabancaria:
    def __init__(self, titular, saldo, tipo_de_cuenta):
        self.titular = titular
        self.saldo = saldo
        self.tipo_de_cuenta= tipo_de_cuenta
    def depositar(self, dinero):
        self.saldo = self.saldo + dinero
    def retirar(self, dinero):
        self.saldo = self.saldo-dinero
    def mostrar_saldo(self):
        print (self.saldo)
    def tipoDeCuenta(self):
        print(self.tipo_de_cuenta)
c1 = cuentabancaria("daniel", 300, "corriente")
c1.depositar(100)
c1.retirar(250)
c1.mostrar_saldo()
c1.tipoDeCuenta()