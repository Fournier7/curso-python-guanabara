import random
opcoes = ['pedra', 'papel', 'tesoura']
computador = random.choice(opcoes)
jogador = input('Digite pedra, papel ou tesoura: ')

print(f'Computador escolheu: {computador}')

if jogador == computador:
    print('Empate!')
elif jogador == 'pedra' and computador == 'tesoura':
    print('Voce ganhou!')
elif jogador == 'papel' and computador == 'pedra':
    print('Voce ganhou!')
elif jogador == 'tesoura' and computador == 'papel':
    print('Voce ganhou!')
else:
    print('Voce perdeu!') 