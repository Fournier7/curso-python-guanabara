peso = float(input('Qual o seu peso? (KG)' ))
altura = float(input('Qual a sua altura? (m)' ))
imc = peso / (altura ** 2 )
print ('O IMC dessa pessoa é de {:.1f}'.format (imc))
if imc < 18.5:
   print ('Voce está abaixo do seu peso normal')
elif 18.5 <= imc < 25:
    print ('Voce est6á no seu peso ideal')
elif 25 <= imc < 30:
    print ('voce está em sobrepeso')
elif 30 <= imc < 40:
    print ('voce está em obesidade')
else:
    print ('voce está em obesidade mórbida')
     

