while True:
    numero = int(input('Diga um numero para ver sua tabuada: '))
    if numero < 0:
        break
    for c in range (1,11):
        resultado = numero * c
        print(f'{numero} x {c} = {resultado}')
