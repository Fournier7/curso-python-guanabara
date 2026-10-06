ficha = []
while True:
    nome = str(input('nome: '))
    nota1 = float(input('nota 1: '))
    nota2 = float(input('nota 2: '))
    media = (nota1 + nota2 ) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print (f'{'No.':<4}{'NOME':<10}{'MÉDIA':>8}')
for i, a in enumerate (ficha):
    print (f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    nota_aluno = int(input('mostrar nota de aluno? (999 para parar):    '))
    if nota_aluno == 999:
        break
    if nota_aluno <= len(ficha) - 1:
        print (f'nota de {ficha [nota_aluno][0]} sao {ficha[nota_aluno][1]}')



