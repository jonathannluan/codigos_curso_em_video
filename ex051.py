a1=int(input('Informe o primeiro Termo dessa PA: '))
r=int(input('Informe a razão dessa PA:'))
print('Os termos dessa PA são:')
for c in range(0,10):
        print('{}'.format(a1+c*r),end=' ')
