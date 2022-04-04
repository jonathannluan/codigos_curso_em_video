from random import randint
print('-='*20)
print('VAMOS JOGAR PAU OU ÍMPAR')
print('-='*20)
aux = ''
cont=0
while True:
    n=int(input('Escolha um número de 1 a 10: '))
    esc=str(input('Escolha par ou ímpar [P/I]: ')).strip().upper()
    pc=randint(1,10)
    if (n+pc)%2 == 0:
        aux = 'P'
        print(f'Você jogou {n} o computador jogou {pc}.O total de {n + pc} deu Par .')
    else:
        aux='I'
        print(f'Você jogou {n} o computador jogou {pc}.O total de {n + pc} deu Ímpar .')
    if esc!=aux:
        break
    else:
        print('Você acertou')
        print('Vamos jogar novamente')
        cont+=1
print(f'Game Over! Você venceu {cont} partidas')


