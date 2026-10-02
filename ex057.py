soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
tot_mulher20 = 0
for c in range(1, 5):
    print (' nome da {} pessoa'.format(c))
    nome = str(input('nome: ' )).strip()
    idade = int(input('idade: '))
    sexo = str(input('sexo [M/F]: ' )).strip()
    soma_idade += idade
    if c == 1 and sexo in 'Mm':
       maior_idade = idade
       nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        tot_mulher20 += 1

mediaidade = soma_idade / 4
print ('a média da idade do grupo é {} anos'.format(media_idade))
print ('o homem mais velho tem {} anos e se chama {}'.format(maior_idade_homem, nome_velho))
print ('ao todo sao {} mulheres com menos de 20 anos'.format(tot_mulher20))


