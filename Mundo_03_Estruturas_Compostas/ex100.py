def maior (* num):
    cont = maior = 0
    print ('-' * 30)
    print ('\nOs valores informados sao:')
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print (f' foram informados {cont} valores.')
    print (f' maior valor foi {maior}')


#Programa principal
maior (5, 5, 6, 7, 8)
maior(2, 3, 4, 5, 7)
maior(4, 5, 6, 7)
maior(6)

