
maior=0
menor=1000
for n in range(1,6):
    p=float(input('Informe o peso da {}ª pessoa: '.format(n)))
    if n==1:
        maior=p
        menor=p
    elif p>maior:
        maior=p
    elif p<menor:
        menor = p

print('O maior peso é {} kg e o menor é {} kg . '.format(maior, menor))
