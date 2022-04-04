from datetime import date
atual = date.today().year
maior=0
menor=0
for n in range(1,8):
    ano=int(input('Infome o ano de nascimento da {}° pessoa. '.format(n)))
    idade = atual - ano
    if idade > 17:
        maior+=1
    else:
        menor+=1
print('Desse grupo, {} são maiores de idade.'.format(maior))
print('Desse grupo, {} são menores de idade.'.format(menor))