import random
from time import sleep
itens=('Pedra','Tesoura','Papel')

print('SUAS OPÇÕES:')
print('[ 0 ] PEDRA.')
print('[ 1 ] TESOURA')
print('[ 2 ] PAPEL')
opc=int(input('Qual sua escolha?'))
pc=random.randint(0,2)

print ('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

print('-='*11)
print('O computador jogou {} .'.format(itens[pc]))
print('Você jogou {} .'.format(itens[opc]))
print('-='*11)

if opc==0:
    if pc==0:
        print('EMPATOU')
    elif pc==1:
        print('VENCEU')
    elif pc==2:
        print('PERDEU')
if opc==1:
    if pc==0:
        print('PERDEU')
    elif pc==1:
        print('EMPATOU')
    elif pc==2:
        print('VENCEU')
if opc==2:
    if pc == 0:
        print('VENCEU')
    elif pc == 1:
        print('PERDEU')
    elif pc == 2:
        print('EMPATOU')


