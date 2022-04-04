from time import sleep
def contador(a,b,c):
    if c<0:
        c*=-1
    if c==0:
        c=1
    if a<b:
        x=a
        while x <= b:
            print(f'{x}',end=' ')
            x+=c
            sleep(0.5)
        print('FIM')
        print('-'*30)
    else:
        x=a
        while x>=b:
            print(f'{x}',end=' ')
            x-=c
            sleep(0.5)
        print('FIM')
        print('-'*30,end=' ')


contador(1,10,1)
contador(10,0,2)
print('-'*30)
print('Agora é com Você')
i=int(input('Início: '))
f=int(input('Fim: '))
p=int(input('Passo: '))
contador(i,f,p)


