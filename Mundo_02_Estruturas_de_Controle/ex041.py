nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2)/ 2

if media < 5:
    print ('Voce foi reprovado!')
elif media >= 5 and media <= 6.9:
    print ('Voce está de recuperaçao!')
else:
    print ('Voce foi aprovado!')