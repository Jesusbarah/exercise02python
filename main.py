from finanzas import Cuenta, Ingresos, Egresos


print("\nInicio Finanzas personales:\n")

finanzasCuenta = Cuenta()
finanzasIngresos = Ingresos()
finanzasEgresos = Egresos()


def crearCuenta():
    finanzasCuenta.openCuenta()


def ingresar():
    ingreso = round(float(input("\n¿Cuánto ingresará? ")), 2)
    finanzasIngresos.addIngreso(ingreso)
    finanzasCuenta.addMovimiento("ingreso", ingreso)


def egresar():
    egreso = (round(float(input("\n¿Cuánto egresará? ")), 2)) * -1
    finanzasEgresos.addEgreso(egreso)
    finanzasCuenta.addMovimiento("egreso", egreso)


def verIngresos():
    finanzasIngresos.getIngresos()


def verEgresos():
    finanzasEgresos.getEgresos()


def verMovimientos():
    finanzasCuenta.getCuenta()


def verSaldo():
    finanzasCuenta.getSaldo()


while True:
    Menu = """\nIngrese el número de la opción que desee ejecutar:
    0-Salir de la aplicación
    1-Crear cuenta
    2-Realizar ingreso
    3-Realizar egreso
    4-Solicitar ingresos
    5-Solicitar egresos
    6-Solicitar todas las transacciones
    7-Solicitar saldo en la cuenta\n"""
    print(Menu)
    opcion = int(input("\n¿Qué opción desea ejecutar? "))
    if opcion == 0:
        print("\nNos vemos a la próxima\n")
        break
    elif opcion == 1:
        crearCuenta()

    elif opcion == 2:
        ingresar()

    elif opcion == 3:
        egresar()

    elif opcion == 4:
        verIngresos()

    elif opcion == 5:
        verEgresos()

    elif opcion == 6:
        verMovimientos()

    elif opcion == 7:
        verSaldo()