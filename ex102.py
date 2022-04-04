def fatorial(a,show=False):
    """
    Função que retorna o Fatorial de um número
    :param a: O número que se deseja saber o fatorial
    :param show: Opcional (true: retorna os cáculos. False: retorna apenas o valor)
    :return: retorna o valor do fatorial
    """
    l=1
    for n in range(a,0,-1):
        if show == True:
            print(n, end='')
            if n > 1:
               print (' x ', end='')
            else:
               print(' = ', end='')
        l*=n
    return l


print(fatorial(9,True))


help(fatorial)
