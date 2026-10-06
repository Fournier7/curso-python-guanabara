produtos = ('caneta', 2.00, 'espelho', 20.00, 'coca', 30.00)
print(f'{"Produto":<10}{"Preco":>10}')
print('-' * 20)
for c in range(0, len(produtos), 2):
    nome = produtos[c]
    preco = produtos[c + 1]
    print(f'{nome:<10}R${preco:>8.2f}')
