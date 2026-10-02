termo = int(input('termo: '))
razao = int(input('razao: '))
contador = 1

while contador <= 10:
    print('{} >'.format(termo), end=' ')
    termo += razao
    contador += 1
print ('FIM')

