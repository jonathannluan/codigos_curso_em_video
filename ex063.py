n=int(input('Escreva quantos termos da série de Fibonacci você quer: '))
a1=0
a2=1
cont=3
print(a1,'->', end=' ')
print(a2,'->', end=' ')
while cont<n:
    termo = a1 + a2
    a1=a2
    a2=termo
    cont+=1
    print(termo,'->', end=' ')

