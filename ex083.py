n=str(input('Informe a expressão: ')).strip()
lista=[]
for x in n:
    if x=='(':
        lista.append('(')
    elif x==')':
        if len(lista) >0:
            lista.pop()
        else:
            lista.append(')')
if len(lista) ==0:
    print('Sua expressão é válida.')
else:
    print('Sua expressão é inválida.')


