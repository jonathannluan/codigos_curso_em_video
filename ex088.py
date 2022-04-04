from random import randint
from time import sleep
num=int(input('Quantos jogos você quer que eu sorteie?'))
lista = []
for n in range(0,num):
    cont=0
    while True:
        ale = randint(1,60)
        if ale not in lista:
            lista.append(ale)
            cont+=1
        if cont>=6:
            break
    lista.sort()
    print (f'Jogo {n+1} : {lista}')
    sleep(2)
    lista.clear()


