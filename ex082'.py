par=[]
impar=[]
total=[]
c=0
while True:
    total.append(int(input('Informe o valor: ')))
    r = str(input('Deseja continuar digitando? [S/N]'))
    if r in 'Nn':
        break
for n in total:
    if n%2==0:
        par.append(n)
    else:
        impar.append(n)
print(total)
print(par)
print(impar)



