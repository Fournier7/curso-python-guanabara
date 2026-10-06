from random import randint
cont = 0
while True:
    numero = int(input('escolha um numero para jogarmos: '))
    escolha_jogador = str(input('par ou impar?')).strip().upper()
    escolha_comp = randint(0,10)
    soma = numero + escolha_comp
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    if escolha_jogador == resultado:
        cont += 1
        print('voce ganhou!')
    else:
        break

print (f'Parabens, voce teve {cont} vitorias consecutivas')

