import math

v = int(input('Informe a velocidade que o carro estava:'))
if v>80:
    print('Você estava acima da velocidade permitida.')
    print('Você irá pagar uma multa de R$ {:.2f} reais.'.format((v-80)*7) )
else:
    print('Você estava viajando dentro do limite de velocidade.')