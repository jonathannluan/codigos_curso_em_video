par=[]
impar=[]
total=[]
while True:
    n=int(input('Informe o valor: '))
    if n%2==0:
        par.append(n)
    else:
        impar.append(n)
    r = str(input('Deseja continuar digitando? [S/N]'))
    if r in 'Nn':
        break
total=par+impar
print(f'A lista completa é {total}')
print(f'A lista dos números pares é: {par} ')
print(f'a lista dos números ímpares é:{impar} ')