print('-'*20)
print('NOTA FISCAL DE PRODUTOS')
print('-'*20)
cont=soma=aux=menor=0
barato=' '
while True:
    nome=str(input('Nome do produto: '))
    valor=float(input('Preço do produto: '))
    if aux==0:
        menor=valor
        barato=nome
        aux+=1
    opc=' '
    soma+=valor
    if valor < menor:
        menor=valor
        barato=nome
    if valor>1000:
        cont+=1
    while opc not in 'SN':
        opc=str(input('Deseja continuar [S/N]? ')).strip().upper()
    if opc=='N':
        break
print(f'O total de compras foi de R${soma} reais!')
print(f'Você comprou {cont} prdotuos acima de R$ 1000.00 !')
print(f'O produto mais barato foi o {barato} que custou R$ {menor} reais!')
