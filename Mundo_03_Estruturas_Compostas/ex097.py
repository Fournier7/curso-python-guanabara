def area (larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {a} m².')


print('CONTROLE DE TERRENOS')
print('-' * 30)
largura = float(input('Digite a largura (m): '))
comprimento = float(input('Digite o comprimento (m): '))
area(largura, comprimento)
