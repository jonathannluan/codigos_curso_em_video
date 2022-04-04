from random import randint
from time import sleep
from operator import itemgetter
dado={'jogador 1':randint(1,6),
      'jogador 2':randint(1,6),
      'jogador 3':randint(1,6),
      'jogador 4':randint(1,6)}
for k,n in dado.items():
    print(f'O {k} tirou {n}')
    sleep(1)
ranking=[]
ranking=sorted(dado.items(),key=itemgetter(1),reverse=True)
print(ranking)
for k,n in enumerate(ranking):
    print(f'O {k+1}º lugar ficou com: {n[0]} com {n[1]}')






