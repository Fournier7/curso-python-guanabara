from random import randint
tentativas = 1
numero = randint(0, 10)
chute = int(input ('Digite um numero entre 0 e 10: '))
while numero != chute:
    print ('Tente novamente!' )
    chute = int(input('Digite outro numero entre 0 e 10: '))
    tentativas += 1
if chute == numero:
    print ('Parabens, voce acertou!')
    print ('Voce acertou o numero e precisou de {} tentativas'.format(tentativas))
