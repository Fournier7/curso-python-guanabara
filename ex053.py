numero = int(input('Digite um numero: '))
primo = True

for c in range(2, numero):
    if numero % c == 0:
        primo = False

if primo:
    print('é um numero primo')
else:
    print('Nao é um numero primo')