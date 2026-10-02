ano = int(input('Digite o ano de: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print ('{} é bissexto!'.format(ano))
else:
    print ('{} nao é bissexto'.format(ano))
    

    