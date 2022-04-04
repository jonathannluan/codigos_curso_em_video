n1=float(input('Informe a primeira nota:'))
n2=float(input('Informe a segunda nota: '))

med=(n1+n2)/2
if med < 5:
    print(' O aluno está REPORVADO, com média {:.1f}!'.format(med))
elif med<7:
    print('O aluno está de RECUPERAÇÃO, com média {:.1f}!'.format(med))
else:
    print('O aluno está APROVADO, com média {:.1f}!'.format(med))