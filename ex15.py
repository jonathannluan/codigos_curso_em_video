dias= int(input('Informe a quantidade de dias alugados: '))
km=float(input('Informe a quantidade de quilômetros rodados: '))
valor= dias*60 + km*0.15
print('O valor pago será de R$ {}'.format(valor))

