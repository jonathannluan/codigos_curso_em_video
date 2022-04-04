from random import randint

pc=randint(0,10)
n=0
while n != pc:
    n=int(input('Qual o número que o pc pensou?'))
    pc=randint(1,3)
    if n != pc:
        print('Você errou, o computador pensou em {} '.format(pc))

print('Você acertou, o computador pensou em {} '.format(pc))
