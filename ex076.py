num = (int(input('Digite o 1º valor: ')),
int(input('Digite o 2º valor: ')),
int(input('Digite o 3º valor: ')),
int(input('Digite o 4º valor: ')))

print(f'o numero 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'o valor 3 foi digitado na posiçao: {num.index(3)+1}')
else:
    print('o valor 3 nao foi digitado')

for n in num:
    if n % 2 == 0:
        print (f'{n} é um numero par')
