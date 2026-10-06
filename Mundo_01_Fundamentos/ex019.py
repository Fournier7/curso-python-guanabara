from math import sin,  cos, tan, radians
num = float(input('digite um numero: '))
rad = radians(num)
seno = sin(rad)
cos = cos(rad)
tang= tan(rad)
print ('o seno desse numero é {:.2f}, o cosseno {:.2f}, e a tangente {:.2f}'.format(seno, cos, tang))
