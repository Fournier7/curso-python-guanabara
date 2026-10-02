from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6),}

ranking = list ()
for k, v in jogadores.items():
    sleep(0.5)
    print(f'O jogador {k} tirou {v} no dado')
    sleep(0.5)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('='*40)
print ('Ranking dos jogadores:')
for i, v in enumerate(ranking):
    print (f'{i+1} lugar,{v[0]} com {v[1]}')
    sleep(0.5)