i=int(input('Informe a sua idade: '))

if i==18:
    print('Você chegou na idade certa para o alistamento')
elif i>18:
    print('Você já deveria ter se alistada à {} anos.'.format(i-18))

else:
    print('Você poderá se alista daqui à {} anos.'.format(18-i))
