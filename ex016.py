km = float(input('Qual a quantidade de KM? '))
dias = int(input('Qual a quantidade de dias? '))
pago = (dias * 60) + (km * 0.15)
print('O Total a pagar será de R${:.2f}'.format(pago))
