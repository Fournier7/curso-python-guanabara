produto = float(input('valor do produto: R$'))
a_vista = produto - (produto * 20 / 100)
parcela = produto - (produto * 2 / 100)
print ('Se o produto custa R${:.2f}, a vista ele vai custar R${:.2f} e parcelado R${:.2f}.'.format(produto, a_vista, parcela))
