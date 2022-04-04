soma=int(0)
cont=0
for n in range(3,500,3):
    if n%2 !=0:
        soma+=n
        cont=cont+1

print('A soma dos {} valores é {} .'.format(cont,soma))

