import random

compra = input ('Valor de la compra ')
cupo = 1000000
numeroCuotas = input ('Número de cuotas ')
valorCuota = int(compra) / int(numeroCuotas)


while compra != 0:
    compra = int(compra) - int(valorCuota)
    if int(compra) > 0:
        print(f"valor de la cuota = {valorCuota}, saldo = {compra}, cupo = {int(cupo) - int(compra)} ")
    else:
        print(f"has pagado tu crédito, tu cupo es de {cupo}")