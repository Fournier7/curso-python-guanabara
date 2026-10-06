from datetime import date
nascimento = int(input('Digite o ano de nascimento: '))
idade= date.today().year - nascimento

if idade <=9:
    print ('Mirim')
elif idade <=14:
    print ('Infantil')
elif idade <=19:
    print ('Junior')
elif idade <=20:
    print ('Senior')
else:
    print ('Master')