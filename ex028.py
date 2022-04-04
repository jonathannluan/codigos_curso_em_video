import random
num=random.randint(0,5)
print('O computador pensou em um número entre 0 e 5.')
p = int(input(' Qual número ele pensou?'))

if p == num:
    print('Parabéns, você acertou, ele escolheu o número {}'.format(num))
else :
    print('Você errou, o número que ele pensou foi o {}'.format(num))

print('---FIM---')