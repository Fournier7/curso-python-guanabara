produto = float(input('valor do produto: R$'))
a_vista = produto - (produto * 10 / 100)
juros_da_parcela = produto + (produto * 10 / 100)
print ('se o produto custa {:.2f}, a vista ele vai custar {:.2f}, e parcelado em 10x de {:.2f}'.format(produto, a_vista, juros_da_parcela / 10))