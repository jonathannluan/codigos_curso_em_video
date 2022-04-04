d=int(input('Informe a distância da viagem em km.'))

if d<=200 :
    print('A viagem irá custar R$ {:.2f} reais'.format(d*0.5))
else:
    print('A viagem irá custar R$ {:.2f} reais.'.format(d*0.45))
