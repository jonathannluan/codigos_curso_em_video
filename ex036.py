casa=float(input('Qual o valor da casa?'))
sal=float(input('Quanto você recebe de salário?'))
tempo=int(input('Em quantos anos você pretende pagar a casa?'))

men=casa/(tempo*12)

if men>sal*0.3:
    print('Seu empréstimo foi negado')
else:
    print('Você irá pagar parcelas de R$ {:.2f} reais'.format(men))

