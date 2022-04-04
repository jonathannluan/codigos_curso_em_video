matriz=[[0,0,0],[0,0,0],[0,0,0]]
soma=terc=maior=0
for n in range (0,3):
    for x in range(0,3):
        matriz[n][x]=int(input(f'Digite o valor [{n} , {x}]'))
        if matriz[n][x]%2==0:
            soma+=matriz[n][x]
        if x==2:
            terc+=matriz[n][x]
        if n==0:
            maior= matriz[n][x]
        if n==1 and matriz[n][x]>maior:
            maior=matriz[n][x]
for n in range(0,3):
    for x in range(0,3):
        print(f'[{matriz[n][x]:^5}]',end='')
    print()
print(f'A soma dos elementos pares é {soma}. ')
print(f'A soma dos elementos da terceiro coluna é {terc}')
print(f'O maior elemento da segunda linha é {maior} ')
