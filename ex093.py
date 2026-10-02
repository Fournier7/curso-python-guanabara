from datetime import date

pessoa = dict()

pessoa ['nome'] = (input('Nome: '))
nasc = int(input('ano do nascimento: '))
pessoa ['Idade'] = date.today().year - nasc
pessoa ['ctps'] = int(input('digite o numero do seu CTPS (tecle 0 se nao tiver): '))


if pessoa ['ctps'] != 0:
    pessoa ['ctps'] = pessoa ['ctps']
    pessoa ['ano_de_contratacao'] = int(input('ano de contratacao: '))
    pessoa ['salario'] = float(input('salario: '))
    pessoa ['aposentadoria'] = pessoa ['idade'] + ((pessoa ['ano_de_contratacao'] + 35) - date.today().year)
print ('==' * 40)
for k, v in pessoa.items():
    print(f'{k} = {v}')
