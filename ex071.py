c50=c20=c10=c1=0
resto=0
valor=int(input('Qual valor você deseja sacar?'))
if valor>50:
    c50=valor//50
    resto=valor-50*c50
if resto>20:
    c20=resto//20
    resto=resto-20*c20
if resto > 10:
    c10=resto//10
    resto=resto-10*c10
if resto>0:
    c1=resto
if c50 != 0:
    print(f'Total de {c50} cédulas de 50')
if c20 != 0:
    print(f'Total de {c20} cédulas de 20')
if c10 != 0:
    print(f'Total de {c10} cédulas de 10')
if c1 != 0:
    print(f'Total de {c1} cédulas de 1')



