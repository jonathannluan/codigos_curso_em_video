num=(int(input('Digite um número')),
     int(input('Digite um número')),
     int(input('Digite um número')),
     int(input('Digite um número')),)
if num.count(9) == True:
    print(f'O número 9 apareceu {num.count(9)} vezes.')
else:
    print('O número 9 não apareceu!')
if num.index(3)==True:
    print(f'O número 3 apareceu na {num.index(3)+1}ºposição.')
else:
    print('O número 3 não foi digitado!')
par=0
print('Os números pares que você digitou foram:',end='')
for n in num:
    if n%2==0:
        print(n)
