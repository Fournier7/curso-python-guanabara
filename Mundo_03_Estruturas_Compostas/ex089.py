from random import randint
from time import sleep

jogos = []
jogo = []
quantos = int(input('Quantos jogos você quer que eu sorteie? '))

for c in range(quantos):
    while len(jogo) < 6:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()

print('Sorteando os seus números...')
sleep(1)

for i, jogo in enumerate(jogos):
    print(f'Jogo {i+1}: {jogo}')
    sleep(1)

print('Boa sorte!')
