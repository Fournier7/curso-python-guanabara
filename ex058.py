sexo = str(input('digite seu sexo (F/M): ')).strip().upper() [0]
while sexo != 'F' and sexo != 'M':
    sexo = str(input('dados invalidos. Digite novemente: ')).strip().upper() [0]
print('sexo {} registrado com sucesso'.format(sexo))