from random import randint

def sorteia (lista):
    for c in range(0,5):
        n = randint(0,10)
        lista.append(n)
    print(f'Os numeros sorteados foram: {lista}')


def somapar (lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'Somando os valores pares de {lista}, temos: {soma}')

numeros = []
sorteia(numeros)
somapar(numeros)
