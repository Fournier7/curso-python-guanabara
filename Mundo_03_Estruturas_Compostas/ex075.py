from random import randint
numero = randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5)
print (f'o numero sorteado foi {numero}')

menor = min(numero)
maior = max(numero)
print (f'o maior numero foi: {maior}')
print (f'o menor numero foi: {menor}')