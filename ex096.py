time = []
jogador = dict()
while True:
    jogador.clear()
    gols = list()
    jogador ['Nome'] = str(input('Nome: '))
    jogador ['partidas'] = int(input('Quantas partidas ele jogou: '))


    for g in range(1, jogador['partidas'] + 1):
        gols_partida = int(input(f'Quantos gols na partida {g}? '))
        gols.append(gols_partida)

    jogador['Gols'] = gols[:]
    jogador['total de gols'] = sum(gols)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        else:
            print ('Digite apenas S ou N.')
    if resp == 'N':
        break

for i in jogador.keys():
    print (f'{i:<15}', end= '')
print ()

print('=-'*40)
for k, v in enumerate(time):
    print (f'{k:>2} ', end='')
    for d in v.values():
        print (f'{str(d):<15}', end='')
    print ()
print('=-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print (f' -- ERRO! nao existe jogador com o codigo {busca}!')
    else:
        print (f' -- levantamento jogador {time[busca], jogador ['Nome']} --')
        for i, g in enumerate(time[busca]['Gols']):
            print (f' no jogo {i+1} fez {g} gols!')

