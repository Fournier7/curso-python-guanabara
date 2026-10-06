aluno = dict()
aluno['nome'] = (input('Nome: '))
media = float(input('Média:  '))
aluno ['media'] = media

if media >= 7:
    aluno['Situacao'] = 'Aprovado'
if media >= 5:
    aluno['Situacao'] = 'Recuperaçao'
else :
    aluno['Situacao'] = 'Reprovado'
print('-=' *35)
for k, v in aluno.items():
    print(f'{k} = {v}')

