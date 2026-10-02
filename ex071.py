produtos_maior_1000 = menor_preço = cont = total =  0
nome_produto_mais_barato = ''

while True:
    produto = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o valor do produto: '))

    if valor > 1000:
        produtos_maior_1000 += 1

    if cont == 0 or valor < menor_preço:
        menor_preço = valor
        nome_produto_mais_barato = produto

    total += valor

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp != 'S':
        break

print(f'o total gasto na compra foi de R$ {total:.2f}')
print(f'{produtos_maior_1000} produtos custam mais de 1.000 reais')
print(f'o produto mais barato foi {nome_produto_mais_barato}')
