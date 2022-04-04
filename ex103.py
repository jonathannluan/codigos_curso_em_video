def ficha(nome='<desconhecido>',gol=0):
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato. ')


#Programa principal
n=str(input('Nome do jogador: '))
g=input('Quantidade de gols: ')

if g.isnumeric():
    g=int(g)
else:
    g=0
if n.strip()=='':
    ficha(gol=g)
else:
    ficha(nome=n,gol=g)