n=1
cont=soma=0
while n!=999:
    n = int(input('Digite um valor (digite 999 para parar): '))
    if n==999:
        break
    soma+=n
    cont+=1
print(f'A soma dos {cont} valores é {soma}')

