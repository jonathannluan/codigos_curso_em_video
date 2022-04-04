from datetime import datetime
dic={}
dic['nome']=str(input('Nome: '))
dic['ano']=int(input('Ano de nascimento: '))
dic['clt']=int(input('Carteira de trabalho: (0 caso não tenha)  '))
dic['idade']= datetime.now().year - dic['ano']
if dic['clt']!=0:
    dic['contrato']=int(input('Ano de contratação: '))
    dic['salario']=int(input('Salário: '))
    dic['aposentar']=dic['idade']+((dic['contrato']+35)-datetime.now().year)
    for n,x in dic.items():
        print(f'{n} tem valor {x}')
else:
    for n,x in dic.items():
        print(f'{n} tem valor {x}')
