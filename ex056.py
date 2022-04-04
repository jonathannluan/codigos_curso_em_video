nome=''
idade=0
s=''
soma=0
aux=0
for p in range(1,5):
    print('-='*11)
    print('{}ª PESSOA'.format(p))
    print('-='*11)
    n=str(input('NOME: ')).strip()
    i=int(input('IDADE: ')).strip()
    soma+=i
    s=str(input('SEXO(M/F): ')).upper().strip()
    if s== 'M' and i>idade:
        nome=n
    if s=='F' and idade<20:
        aux+=1
    idade=i
print('A média das idades é {} '.format(soma/4))
print('O homem mais velho é {}'.format(nome))
print('Existem no total {} mulheres com menos de 20 anos'.format(aux))