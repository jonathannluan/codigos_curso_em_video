import math

r1=int(input('Informe o comprimento da primeira reta: '))
r2=int(input('Informe o comprimento da segunda reta: '))
r3=int(input('Informe o comprimento da terceira reta: '))

if math.sqrt(((r1-r2)**2))<r3 and (r1+r2)>r3:
    print('É possível fazer um triângulo com essas retas')
else:
    print('Não é possivel fazer um triângulo com essas retas')