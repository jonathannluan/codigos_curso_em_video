maior=homem=mulher=0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade=int(input('IDADE:'))
    sexo=' '
    while sexo not in 'MF':
        sexo=str(input('SEXO [M/F]: ')).strip().upper()

    if idade >=18:
        maior+=1
    if sexo=='M':
        homem+=1
    if sexo=='F' and idade <20:
        mulher+=1
    opc = ' '
    while opc not in 'SN':
        opc=str(input('Deseja continuar cadsatrando[S/N]?')).strip().upper()
    if opc=='N':
        break
print(f'{maior} pessoas são maiores de idade')
print(f'Foram cadastrados {homem} homens.')
print(f'{mulher} mulheres tem menos de 20 anos')

