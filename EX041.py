idade=int(input('Informe o valor da sua idade: '))

if idade <10:
    print('Categoria MIRIM')
elif idade <15:
    print('Categoria INFANTIL')
elif idade<20:
    print('Categoria JÚNIOR')
elif idade<25:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')