termo = int(input('termo: '))
razao = int(input('razao: '))
décimo = termo + (10 - 1 ) * razao

for c in range(termo, décimo + razao, razao):
    print('{}'.format(c), end=' ')

