class Cuenta:
    def __init__(self):
        self.cuentaList = []
        self.saldo = 0.00

    def openCuenta(self):
        apertura = {"movimiento": "apertura", "monto": 0.00}
        self.cuentaList.append(apertura)
        print("\nSe inició la cuenta correctamente\n")

    def addMovimiento(self, movimiento, monto):
        movimiento = {"movimiento": movimiento, "monto": monto}
        self.cuentaList.append(movimiento)

    def getCuenta(self):
        print("\nSus movimientos son los siguientes:\n")
        for iterador in self.cuentaList:
            print(iterador)

    def getSaldo(self):
        print("\nSu saldo total es el siguiente:\n")
        for iterador in self.cuentaList:
            self.saldo += iterador.get("monto")
        print(self.saldo)


class Ingresos:
    def __init__(self):
        self.IngresosList = []

    def addIngreso(self, ingreso):
        nuevoIngreso = {"movimiento": "ingreso", "monto": ingreso}
        self.IngresosList.append(nuevoIngreso)
        print("\nSe realizó su ingreso correctamente\n")

    def getIngresos(self):
        print("\nSus ingresos son los siguientes:\n")
        for iterador in self.IngresosList:
            print(iterador)


class Egresos:
    def __init__(self):
        self.EgresosList = []

    def addEgreso(self, egreso):
        nuevoEgreso = {"movimiento": "egreso", "monto": egreso}
        self.EgresosList.append(nuevoEgreso)
        print("\nSe realizó su egreso correctamente\n")

    def getEgresos(self):
        print("\nSus egresos son los siguientes:\n")
        for iterador in self.EgresosList:
            print(iterador)