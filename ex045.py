produto = float(input('Digite o valor do produto: '))
print ('''Forma de pagamento: 
[ 1 ] a vista dinheiro/cheque 
[ 2 ] a vista no cartao 
[ 3 ] 2x no cartao 
[ 4 ] 3x ou mais no cartao''')

opçao = int(input('qual a opçao?'))


if opçao == 1:
    print('Total: R${:.2f}'.format(produto * 0.90))
elif opçao == 2:
    print('Total: R${:.2f}'.format(produto * 0.95))
elif opçao == 3:
    print('Total: R${:.2f}'.format(produto * 1.00))
elif opçao == 4:
    print('Total: R${:.2f}'.format(produto * 1.20))
