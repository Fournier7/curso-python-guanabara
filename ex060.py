n1 = int(input('Digite primeiro numero: '))
n2 = int(input('Digite segundo numero: '))

while True:

    print ('''[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa ''')

    opçao = int(input('Escolha uma opçao:' ))

    if opçao  == 1:
        soma = n1 + n2
        print('A soma entre {} e {}, vale {}'.format(n1, n2, soma))
    elif opçao == 2:
        produto = n1 * n2
        print ('A multiplicaçao entre {} e {} vale {}'.format(n1, n2, produto))
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        else :
            maior = n2
        print('o maior numero entre {} e {} é {}'.format(n1, n2, maior))
    elif opçao == 4:
        print('informe os numeros novamente')
        n1 = int(input('Digite primeiro numero: '))
        n2 = int(input('Digite segundo numero: '))
    elif opçao == 5:
        print('fim')
        break
    else:
        print('opçao invalida. tente novamente!')