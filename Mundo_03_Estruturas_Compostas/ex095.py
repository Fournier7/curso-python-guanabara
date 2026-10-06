pessoas = []
mulheres = []
tot_idade = 0

while True:
    pessoa = {}
    pessoa['nome'] = input('Nome: ')
    sexo = input('Qual seu sexo [M/F]? ').strip().upper()[0]
    while sexo not in 'MF':
        sexo = input('inválido. Qual seu sexo [M/F]? ').strip().upper()[0]
    pessoa['sexo'] = sexo

    pessoa['idade'] = int(input('Qual sua idade: '))
    tot_idade += pessoa['idade']
    pessoas.append(pessoa)
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa)

    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break

media = tot_idade / len(pessoas)

print('-=' * 35)
print(f'Ao todo, foram cadastradas {len(pessoas)} pessoas.')
print(f'A média de idade do grupo é {media:5.2f} anos.')
print('Lista de mulheres cadastradas:')
print('-=' * 35)

for m in mulheres:
    print(f' - {m["nome"]}')
print('Pessoas com idade acima da média:')
print('-=' * 35)

for p in pessoas:
    if p['idade'] > media:
        print(f' - {p["nome"]}, {p["idade"]} anos')
