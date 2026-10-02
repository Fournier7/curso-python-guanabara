velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print ('Voce foi multado em R${:.f} por exceder o limite.'.format (multa))
else:
    print('Tenha um bom dia!')
