num=('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','vinte')
while True:
    n=int(input('Digite um número: '))
    if n>0 and n<=20:
        break
print(f'Você digitou o número {num[n]}')
