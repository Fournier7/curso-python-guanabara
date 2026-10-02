Real = float (input('Quando voce tem na carteira? '))
Dolar = Real / 5.02
Euro = Real / 5.85
print ('com R${:.2f}, voce pode comprar US${:.2f} dolares, e €{:.2f}'.format(Real, Dolar, Euro))
