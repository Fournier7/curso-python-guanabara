lista = []
lista_par = []
lista_impar = []
for c in range(1, 8):
    valor = int (input (f'Digite o {c}o valor: '))
    lista.append(valor)

    if valor % 2 == 0:
        lista_par.append(valor)

    else:
        lista_impar.append(valor)

lista_par.sort()
lista_impar.sort()

print(f'Pares: {lista_par}')
print(f'Impares: {lista_impar}')
