
n=int(input('Informe o número'))
div=0
for c in range(1,n+1):
    if n%c==0:
        print('\33[31m', end=' ')
        div=div+1
    else:
        print('\33[m', end=' ')
    print('{}'.format(c),end=' ')
if div > 2:
    print('\33[36m')
    print('O número NÃO É PRIMO')
else:
    print('\33[36m')
    print('O número É PRIMO')
