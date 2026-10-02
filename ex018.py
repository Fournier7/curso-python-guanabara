from math import hypot
cat1 = float(input('digite um numero: '))
cat2 = float(input('digite um numero: '))
hi = hypot(cat1, cat2)
print ('Medindo os catetos {} e {}, a hipotenusa é {:.2f}'.format(cat1, cat2, hi))
