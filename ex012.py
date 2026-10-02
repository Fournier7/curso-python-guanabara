#n = float (input('digite um numero: '))
#n2 = float (input('digite outro numero: '))
#print('Se sua parede tem {} metros de altura e {} metros de largura, voce precisa de {:.2f} litros de tinta'.format(n, n2, (n * n2) / 2))

A = float (input('digite a altura: '))
L = float (input('digite a largura: '))
area = A * L
print ('sua parede tem {}x{}, sua area é de {}m'.format(A, L, area))
tinta = area / 2
print ('para pintar essa parede, voce vai precisar de {} litros de tinta'.format(tinta))
