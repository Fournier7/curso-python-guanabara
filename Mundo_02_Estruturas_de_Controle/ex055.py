from datetime import date
ano = date.today().year
menores = 0
maiores = 0

for c in range(1, 8):
    nasc = int(input('Digite o ano de nascimento: '))
    idade = ano - nasc
    if idade < 18:
        menores += 1
    else:
        maiores += 1

print('Menores:', menores)
print('Maiores:', maiores)




