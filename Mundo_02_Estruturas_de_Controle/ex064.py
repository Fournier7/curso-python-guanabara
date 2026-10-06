n = int(input('Quantos termos: '))
t1, t2 = 0, 1
contador = 0

while contador < n:
    print (t1, end=' > ')
    t1, t2 = t2, t1 + t2
    contador += 1
print ('FIM')