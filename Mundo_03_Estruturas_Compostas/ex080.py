lista = []
while True :
    valor = int(input('Digite um numero: '))
    if valor not in lista :
        lista.append(valor)
        print('Valor adicionado na lista')
    else:
        print('Valor duplicado, digite outro')
    resp = str(input('quer continuar [S/N]? ')).upper().strip()[0]
    if resp == 'N':
        break

print (f'Voce digitou os valores {sorted(lista)}')