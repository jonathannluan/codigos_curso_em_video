n=int(input('Informe o número desejado: '))
fatorial=1
num = n
while n!=0:
    fatorial=fatorial*n
    n=n-1
print('O fatorial de {} é {}.'. format(num,fatorial))