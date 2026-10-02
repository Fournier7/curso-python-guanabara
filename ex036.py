r1 = float(input('primeiro segmento: '))
r2 = float(input ('segundo segmento: ' ))
r3 = float(input ('terceito segmento: ' ))

if r1 < r2 + r3 and r1 + r3 and r3 < r1 + r2:
    print ('eles podem formar um triangulo!')
else:
    print ('eles nao pode formar um triangulo!')
