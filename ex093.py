dados={}
partidas=[]
dados['nome']=str(input('Infomre o nome do jogador: '))
x=int(input('Quantas partidas ele jogou? '))
n=total=0
while n < x:
    partidas.append(int(input(f'Quantos gols ele marcou na jogo {n+1}? ')))
    n+=1
dados['gols']=partidas[:]
dados['total']=sum(partidas)
print('-='*20)
print(dados)
print('-='*20)
for k,y in dados.items():
    print(f'O campo {k} tem valor {y}')
print('-='*20)
print(f'O jogar {dados["nome"]} jogou {x} jogos. ')
m=0
for m in range(0,len(dados)+1):
    print('    =>', end=' ')
    print(f'Na partida {m+1} fez {partidas[m]}')



