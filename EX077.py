palavras=('Bolsa', 'Carteira','Chave','Melancia', 'Violão')

for n in palavras:
    print(f'\nNa Palavra {n.upper()} temos as vogais: ',end='')
    for x in n:
        if x.lower() in 'aáãâeéiíoõôóuú':
            print( x,end='')

