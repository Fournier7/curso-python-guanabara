palavras = ( 'aprender', 'programar', 'linguagem', 'python',
             'curso', 'grupo', 'mercado', 'programador' )
for c in palavras:
    print(f'\n a palavra {c.upper()} temos ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

