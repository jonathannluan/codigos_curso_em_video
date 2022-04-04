dic={}
lista=[]
r='k'
soma=media=0
while True:
    dic['nome']=str(input('Informe o nome: '))
    dic['sexo']=str(input('Sexo[M/F]: ')).upper()
    dic['idade']=int(input('Idade: '))
    soma+=dic['idade']
    r=str(input('Deseja continuar? [S/N]')).strip()
    lista.append(dic.copy())

    if r in 'Nn':
        break
print(f'Foram cadastradas {len(lista)} pessoas. ')
media=soma/len(lista)
print(f'A média das idades é de {media:5.2f}')
print('As mulheres cadastradas foram: ',end=' ')
for n in lista:
    if n['sexo']=='F':
        print(f'{n["nome"]}',end=' ')
print(' ')
print('As idades acima da média, são as de: ',end=' ')
for n in lista:
    if n['idade']>media:
        print('')
        for k,c in n.items():
            print(f'{k} ={c}',end=' ')
        print('')




