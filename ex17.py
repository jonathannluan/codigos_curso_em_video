import math
c1=float(input('Informe o valor do cateto adjacente:'))
c2=float(input('Informe o valor do cateto oposto:'))
h=math.sqrt((c1**2 + c2**2))
print('A hipotenusa desse triângulo é {:.2f} '.format(h))
