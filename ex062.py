a1=int(input('Informe o primeiro termo dessa PA: '))
r=int(input('Informe a razão dessa PA: '))
c=1
total = 0
n=10
cont = 0
while n!=0:
    total=total+n
    while c<=total:
        a1=a1+r
        c+=1
        cont+=1
        print(a1,end='  ')
    print('PAUSA')
    y=1
    n=int(input('Você quer mostrar mais quantos termos? '))
print('PROGRAMA ENCERRADO')
print('Essa progressão apresenta {} termo.'.format(cont))