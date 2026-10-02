jogador = dict()
gols = list()

jogador ['Nome'] = str(input('Nome: '))
jogador ['partidas'] = int(input('Quantas partidas ele jogou: '))

for g in range(1, jogador['partidas'] + 1):
    gols_partida = int(input(f'Quantos gols na partida {g}? '))
    gols.append(gols_partida)

jogador['Gols'] = gols[:]
jogador['total de gols'] = sum(gols)
print('=-'*40)

for k, v in jogador.items():
    print(f'{k} = {v}')
print('=-'*40)

print(f'o jogador {jogador ['Nome']} jogou {jogador ['partidas']} partidas.')
for i, g in enumerate(jogador['Gols']):
    print (f'Na partida {i+1}, fez {g} gols')
print (f'Foi um total de {jogador["total de gols"]} gols.')


