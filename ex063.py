termo = int(input('termo: '))
razao = int(input('razao: '))
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print('{} >'.format(termo), end=' ')
        termo += razao
        contador += 1
    print ('PAUSA')
    mais = int(input('quantos termos voce quer botar a mais? '))
print ('finalizada com {} termos mostrados'.format(total))