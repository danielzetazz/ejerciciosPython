class cuentabancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, dinero):
        self.saldo = self.saldo + dinero
    def retirar(self, dinero):
        self.saldo = self.saldo-dinero
c1 = cuentabancaria("daniel", 300)
c1.depositar(100)
c1.retirar(250)
print (c1.saldo)