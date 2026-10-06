lista = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'foram digitados {len(lista)} valores')
lista.sort(reverse=True)
print(f'{lista}')
if 5 in lista:
    print ('o numero 5 está na lista')
else:
    print('o numero 5 nao está na lista')