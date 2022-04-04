matriz=[[0,0,0],[0,0,0],[0,0,0]]
soma=terc=0
for n in range (0,3):
    for x in range(0,3):
        matriz[n][x]=int(input(f'Digite o valor [{n} , {x}]'))
for n in range(0,3):
    for x in range(0,3):
        print(f'[{matriz[n][x]:^5}]',end='')
    print()




