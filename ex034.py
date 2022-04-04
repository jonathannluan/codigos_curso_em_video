s=float(input('Informe o valor do seu salário: '))

if s>=1250:
    print('Seu aumento será de R$ {:.2f}'.format(s*0.1))
    print('Seu novo salário será R$ {:.2f} '.format(s*1.1))
else:
    print('Seu aumento será de R$ {:.2f}'.format(s*0.15))
    print('Seu novo salário será R$ {:.2f} '.format(s * 1.15))