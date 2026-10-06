numero = int(input('digite um numero: '))

contador = soma = 0

while True:
    numero = int(input('digite um numero: '))
    if numero == 999:
        break
    else :
        soma += numero
        contador += 1

print('voce digitou {} numeros, e a soma deles é, {}'.format(contador, soma))