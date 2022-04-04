soma=cont=0
n=int(input('Informe o valor [digite 999 para parar]'))
while n!=999:
    soma+=n
    cont+=1
    n = int(input('Informe o valor [digite 999 para parar]'))
print('A soma dos {} valores informados é {} . '.format(cont,soma))