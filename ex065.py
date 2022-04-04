r='S'
soma=maior=menor=0
n=int(input('Digite um número: '))
r=str(input('Deseja continuar [S/N]?')).upper().strip()
soma=maior=menor=n
cont=1
while r!='N':
    n=int(input('Digite um número: '))
    soma+=n
    cont+=1
    if n>maior:
        maior=n
    elif n<menor:
        menor=n
    r = str(input('Deseja continuar [S/N]?')).upper().strip()
print('Você digitou {} números e a média foi {:.2f} !'.format(cont,soma/cont))
print('O maior número foi {} e o menor {} !'.format(maior,menor))