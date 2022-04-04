tab=0
while True:
    n=int(input('Quer ver a tabuada de qualquer número?'))
    print('-' * 30)
    if n<0:
        break
    for c in range (1,11):
        tab=n*c
        print(f'{n} x {c} = {tab}')
    print('-' * 30)
print('PROGRAMA ENCERRADO')