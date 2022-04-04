import math
maior= 0
menor =0
n1 = float(input('Informe o primeiro número: '))
maior=n1
menor=n1
n2=float(input('Informe o segundo número:'))
if n2>maior:
    maior=n2
if n2<menor:
    menor=n2

n3=float(input('Informe o terceiro número: '))

if n3>maior:
    maior=n3
if n3<menor:
    menor=n3

print( 'O maior número é o {} e o menor é o {} .'.format(maior,menor))
