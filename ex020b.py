from random import choice

cantor1 = input('primeiro cantor: ')
cantor2 = input('segundo cantor: ')
cantor3 = input('terceiro cantor: ')
cantor4 = input('quarto cantor:')

lista = [cantor1, cantor2, cantor3, cantor4]

escolhido = choice(lista)

print ('O cantor mais bonito é o: {}'.format(escolhido))