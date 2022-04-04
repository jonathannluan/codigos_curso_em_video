r='S'
lista=list()
cont=0
while True:
    x=int(input('Digite o valor: '))
    if x not in lista:
        lista.append(x)
    else:
        print('Valor Duplicado. Não vou adicionar.')
    r=str(input('Deseja continuar [S/N]? ').upper().strip())
    if r=='N':
        break
lista.sort()
print(f'Os valores digitados foram {lista}')



