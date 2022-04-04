dados={}
lista=[]
gol=[]
r='S'
x=total=0
while True:
    dados.clear()
    dados['nome']=str(input('Informe o nome do jogador: ')).strip()
    partidas=int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    for n in range(0,partidas):
        gol.append(int(input(f'Quantos gols ele marcou na partida {n+1}: ')))
    dados['gols']=gol[:]
    dados['total']=sum(gol)
    gol.clear()
    lista.append(dados.copy())
    while True:
        resp=str(input('Deseja Continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('Erro!! Responda apenas S ou N')
    if resp=='N':
        break
print('-='*30)
print('cod ',end='')
for i in dados.keys():
    print(f'{i:<15}',end='')
print()
for k,v in enumerate(lista):
    print(f'{k:>3} ',end=' ')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-'*40)
while True:
    busca=int(input('Mostrar os dados de qual jogador? (999 para parar)'))
    if busca==999:
        break
    if busca >= len(lista):
        print('Valor informado inválido')
    else:
        print(f'Levantamento do jogador {lista[busca]["nome"]}')
        for n,g in enumerate(lista[busca]['gols']):
            print(f'No jogo {n+1} fez {g}')











