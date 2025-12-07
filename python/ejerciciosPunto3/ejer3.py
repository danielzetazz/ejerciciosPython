class cuentabancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
    def depositar(self, dinero):
        self.__saldo = self.__saldo + dinero
    def retirar(self, dinero):
        if (self.__saldo)>=dinero:
            self.__saldo = self.__saldo-dinero
        else: print(f"No hay suficiente saldo, saldo: {self.__saldo}")
    def impSaldo(self):
        print(self.__saldo)
c1 = cuentabancaria("daniel", 300)
c1.depositar(100)
c1.retirar(250)
c1.impSaldo()
c1.retirar(200)
print(c1.__saldo)