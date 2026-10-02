casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salario? R$'))
anos = int(input('Quantos anos deseja pagar? '))
prestaçao = casa / (anos * 12)

if prestaçao <= salario * 30/100:
    print('Emprestimo aprovado! Prestacao de R${:.2f}'.format(prestaçao))
else:
    print('Infelizmente voce nao tem condicoes de pagar')