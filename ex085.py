pessoas = []
dados = []

while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
maior = 0
menor = 999999999
nome_maior = ''
nome_menor = ''
for p in pessoas:
    if p[1] > maior:
        maior = p[1]
        nome_maior = p[0]
    if p[1] < menor:
        menor = p[1]
        nome_menor = p[0]
print (f'foram cadastradas {len(pessoas)} pessoas')
print (f'As pessoas mais pesadas sao {nome_maior} com {maior} KG:')
print (f'As pessoas mais leves sao {nome_menor} com {menor} KG')


