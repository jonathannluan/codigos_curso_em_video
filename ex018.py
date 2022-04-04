import math
a=int(input('Informe o valor do âgulo:'))
sen=math.sin(math.radians(a))
cos=math.cos(math.radians(a))
tg=math.tan(math.radians(a))
print('O seno vale {:.2f} , o cosseno vale {:.2f} e a tangente vale {:.2f}'.format(sen,cos,tg))
