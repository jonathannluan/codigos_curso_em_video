
p=str(input('Informe a frase: ')).strip().upper()
p=p.split()
p=''.join(p)
inverso=''
for a in range(len(p)-1,-1,-1):
    inverso+=p[a]
if inverso==p:
    print('Você escreveu um palíndromo.')
else:
    print('Você não escreveu um palíndromo')