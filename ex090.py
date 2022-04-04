d={}
d['nome']=str(input('Digite o nome: '))
d['media']= float(input(f'Digite a nota de {d["nome"]}: '))
if d['media'] <7:
    d['Situação']='Recuperação'
else:
    d['Situação']='Aprovado'
for n,k in d.items():
    print(f'{n} é igual a {k}')