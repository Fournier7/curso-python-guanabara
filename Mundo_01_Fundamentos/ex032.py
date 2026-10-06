distancia= int(input('Qual a distancia?'))
if distancia <= 200:
    passagem = distancia * 0.50
    print ('Para {}km, o valor foi de R$ {:.2f}'.format(distancia, passagem))
else:
    passagem = distancia * 0.45
    print('Para {}km, o valor foi de R$ {:.2f}'.format(distancia, passagem))