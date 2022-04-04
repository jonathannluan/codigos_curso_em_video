n1=int(input('Informe a medida do primeiro lado: '))
n2=int(input('Informe a medida do segundo lado: '))
n3=int(input('Informe a medida do terceiro lado: '))

if n1==n2 and n1==n3 and n2==n3:
    print('O triângulo é EQUILÁTERO')
elif n1!=n2 and n1!=n3 and n2!=n3:
    print('O triângulo é ESCALENO')
else:
    print('O triângulo é ISÓSCELES')
