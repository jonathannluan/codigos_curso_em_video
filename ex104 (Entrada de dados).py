def leiaInt(a):
    ok=False
    valor=0
    while True:
        n=str(input(a))
        if n.isnumeric():
            valor=int(n)
            ok=True
        else:
            print('Erro!! Digite um número válido')
        if ok:
            break
    return valor


#Programa principal
n=leiaInt('digite um número: ')
print(f' Você digitou o número {n}')