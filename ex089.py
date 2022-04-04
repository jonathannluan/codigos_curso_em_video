lista=[]
r='k'
cont=0
while True:
    nome=str(input('Informe o Nome do aluno: '))
    nota1=float(input('Informe a 1º nota: '))
    nota2=float(input('Informe a 2ª nota: '))
    media=(nota1+nota2)/2
    lista.append([nome,[nota1,nota2],media])
    while r not in 'sSnN':
        r=str(input('Deseja continuar [S/N]'))
    if r in 'Nn':
        break
    r='k'
print('-='*30)
print(f'{"Nº.":<4}{"Nome":<12}{"Média":>8}')
print('-='*30)
for n in range(0,len(lista)):
    print(f'{n:<4}',end='')
    print(f'{lista[n][0]:<12}',end='')
    print(f'{lista[n][2]:>8.1f}',end='')
    print()
print('-='*30)

while True:
    num=int(input('Mostra a nota de qual aluno (nº)?  (999 interrompe)'))
    if num == 999:
        break
    else:
        print(f'A primeira nota foi {lista[num][1][0]}')
        print(f'A segunda nota foi {lista[num][1][1]}')






