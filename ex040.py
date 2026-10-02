from datetime import date
nascimento = int(input('Digite o ano de nascimento: '))
idade= date.today().year - nascimento

if idade < 18:
    print(f'Voce ainda vai se alistar. Faltam {18 - idade} anos.')
elif idade == 18:
    print('Voce precisa se alistar agora!')
else:
    print(f'Voce passou do prazo há {idade - 18} anos.')