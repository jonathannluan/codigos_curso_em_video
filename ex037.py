num=int(input(('Informe um número inteiro.')))
print('Digite o número da base para qual deseja converter esse número?')
print('(1) Binário')
print('(2)Hexadecimal')
print('(3) Octal')
resposta=int(input(''))
if resposta==1:
    print(bin(num))
elif resposta==2:
    print(hex(num))
elif resposta==3:
    print(oct(num))
else:
    print('Digite o número da sua opção')

