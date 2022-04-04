def maior(*num):
    m=0
    for valor in num:
        if m<valor:
            m=valor

    print('Analisando o valores passado... ')
    print(f'{num}  foram informados {len(num)} valores!')
    print(f'O maior valor é o {m} ')
    print('-='*30)


maior(3,5,6,7,8,9,0,1,2,3,4,5,6)
maior(2,8,7,6,5,4,3)