maiores_18 = 0
homens = 0
mulheres_menores_20 = 0
mulheres = 0
resp = 'S'
while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Valor invalido! Digite seu sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
       maiores_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F':
        mulheres += 1
    if sexo == 'F' and idade < 20:
        mulheres_menores_20 += 1
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resp != 'S' and resp != 'N':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp != 'S':
        break
print (f'temos {maiores_18} maiores de 18 anos cadastrados' )
print (f'temos {homens} homens cadastrados' )
print (f'temos {mulheres_menores_20} mulheres menores que 20 anos cadastradas.' )
print (f'temos {mulheres} mulheres cadastradas.' )