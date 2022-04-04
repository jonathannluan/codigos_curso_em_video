lista=[]
aux=0
r='S'
while r in 'Ss':
    n=int(input('Digite uma valor: '))
    lista.append(n)
    if n == 5:
        aux+=1
    r=str(input('Você deseja continuar[S/N]?'))
print('-'*30)
print(f'Você digitou {len(lista)} elementos!')
lista.sort(reverse=True)
print(f'Os valore em ordem decrescente foram {lista}')
if 5 in lista:
    print('O número 5 faz parte dessa lista.')
else:
    print('O número 5 não faz parte dessa lista.')