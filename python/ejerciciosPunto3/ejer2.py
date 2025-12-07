class cuentabancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, dinero):
        self.saldo = self.saldo + dinero
    def retirar(self, dinero):
        if (self.saldo)>=dinero:
            self.saldo = self.saldo-dinero
        else: print(f"No hay suficiente saldo, saldo: {self.saldo}")
    def impSaldo(self):
        print(self.saldo)
c1 = cuentabancaria("daniel", 300)
c1.depositar(100)
c1.retirar(250)
c1.impSaldo()
c1.retirar(200)