salario = float(input('Qual o seu salario: '))
if salario <= 1250:
    salario = salario + (salario * 15/100)
    print ('Seu salario será de {:.2f}.'.format(salario))
else:
    salario = salario + (salario * 10/100)
    print ('Seu salario sera de R${:.2f}.'.format(salario))
