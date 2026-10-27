from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= 1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        for c in range(i, f + 1, p):
            sleep(0.5)
            print(c, end=' ')
    else:
        for c in range(i, f - 1, -p):
            sleep(0.5)
            print(c, end=' ')
    print()

contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é a sua vez de personalizar:')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
sleep(0.5)
contador(ini, fim, pas)
