lista = []
for c in range (0,5):
    valor = int(input('Digite um valor: '))
    lista.append(valor)

maior = max(lista)
menor = min(lista)

pos_maior = lista.index(maior)
pos_menor = lista.index(menor)
print(f'o maior numero foi {maior} e esta na posicao: {pos_maior}')
print(f'o menor numero foi {menor} e esta na posicao: {pos_menor}')
