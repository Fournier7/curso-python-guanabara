from random import randint
numero = randint(0, 5)
chute = int(input ('Digite um numero entre 0 e 5:'))
if chute == numero:
    print ('Parabens, voce acertou!')
else:
    print ('Voce errou, haha!')