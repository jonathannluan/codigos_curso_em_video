op = 0
n1=int(input('Digite o primero valor: '))
n2=int(input('Digite o segundo valor: '))
while op!=5:
    print('[ 1 ] SOMAR')
    print('[ 2 ] MULTIPLICAR')
    print('[ 3 ] MAIOR')
    print('[ 4 ] NOVOS NÚMEROS')
    print('[ 5 ] SAIR DO PROGRAMA')
    op=int(input(' O que deseja fazer com eles?'))
    if op ==1:
        print('A soma desses dois valores é {} .'.format(n1+n2))
    elif op==2:
        print('O produto deles é {} '.format(n1*n2))

    elif op==3:
        if n1>n2:
            print('O maior número é o {} .'.format(n1))
        else:
            print('O maior número é o {} .'.format(n2))
    elif op==4:
        n1 = int(input('Digite o primero valor: '))
        n2 = int(input('Digite o segundo valor: '))
    print('-='*10)
print('PROGRAMA ENCERRADO')

