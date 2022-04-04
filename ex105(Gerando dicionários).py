def notas(*num,sit=False):
    tamanho=len(num)

    maior=cont=soma=0
    for valor in num:
        soma+=valor
        if maior < valor:
            maior = valor
        if cont==0:
            menor=valor
            cont+=1
        elif menor > valor:
            menor = valor
    media=soma/tamanho
    x=''
    if media<6:
       x='Ruim'
    elif 6< media < 7:
        x='Razoável'
    else:
        x='BOA'
    dic={}
    if sit==True:
        dic['Quantidade']=tamanho
        dic['Maior']=maior
        dic['Menor']=menor
        dic['Média']=soma/tamanho
        dic['Situação']=x
    else:
        dic['Quantidade'] = tamanho
        dic['Maior'] = maior
        dic['Menor'] = menor
        dic['Média'] = soma / tamanho

    print(dic)


#programa principal
notas(5.5,8.5,10,7.5,2, sit=True)
print(notas)