valor=float(input('Informe o valor do produto: '))
print('Escolha a forma de pagamento: ')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opc=int(input('Informe a opção desejada: '))

if opc==1:
    print('Você irá pagar R$ {} !'.format(valor*0.9))
elif opc==2:
    print('Você irá pagar R$ {} !'.format(valor*0.95))
elif opc==3:
    print('Você irá pagar R$ {} !'.format(valor))
else:
    print('Você irá pagar R$ {} !'.format(valor*1.2))