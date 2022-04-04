nome=[]
prin=[]
maior=menor=0
resposta='S'

while True:
    nome.append(str(input('Nome: ')).strip())
    nome.append(float(input('Peso: ')))
    if len(prin)==0:
        maior=menor=nome[1]
    else:
        if nome[1]>maior:
            maior=nome[1]
        if nome[1]<menor:
            menor=nome[1]
    prin.append(nome[:])
    nome.clear()
    resposta=str(input('Deseja continuar? [S/N]')).strip()
    if resposta in 'Nn':
        break
print('=-'*30)
print(f'Você cadastrou {len(prin)} pessoas. ')
print(f'O maior peso foi de {maior} Kg. Quem tem Esse peso é ', end='')
for n in prin:
    if n[1]==maior:
        print(f'[{n[0]}] ', end='')
print(f'\n O menor peso foi de {menor} Kg. Quem tem esse peso é ', end='')
for n in prin:
    if n[1]==menor:
        print(f'[{n[0]}] ', end='')
