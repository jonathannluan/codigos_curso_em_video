time=('Palmeiras','Corinthians','Atlético Mineiro',
      'São Paulo','Santos', 'Internacional','Vasco',
      'Fluminense','Bahia','Fortaleza',
      'Sport','América','Cuiabá','Vitória','Chapecoense',
      'Goiás','Alagoano','Flamengo','Portuguesa','Ceará')
print('='*50)
print(f'Lista de times brasileiros{time}')
print('='*50)
print(f'Os cinco primeiros colocados são {time[0:5]}')
print('='*50)
print(f'Os quatro últimos são{time[16:20]}')
print('='*50)
print(f'Os times em orfem alfabética são{sorted(time)}')
print('='*50)
print(f'O chapeconense está {time.index("Chapecoense")+1}º Posicção')
