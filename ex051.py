soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}º numero: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('voce informou {} numeros pares, e a soma foi {}'.format(cont, soma))
